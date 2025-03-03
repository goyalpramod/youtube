#!/usr/bin/env python3
import os
import sys
import inspect
import importlib.util
import subprocess
import argparse

def find_scene_classes(file_path):
    """
    Find all Scene classes in the given Manim Python file.
    
    Args:
        file_path (str): Path to the Manim Python file
        
    Returns:
        list: List of scene class names
    """
    # Validate file path
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist")
        return []
    
    if not file_path.endswith('.py'):
        print(f"Error: File '{file_path}' is not a Python file")
        return []
    
    # Extract file information
    file_dir = os.path.dirname(os.path.abspath(file_path))
    file_name = os.path.basename(file_path)
    module_name = os.path.splitext(file_name)[0]
    
    # Import the module
    try:
        # Add the directory to sys.path to handle imports within the module
        sys.path.insert(0, file_dir)
        
        # Create a spec from the file path
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        # Add the module to sys.modules to handle potential imports within the module
        sys.modules[module_name] = module
        # Execute the module
        spec.loader.exec_module(module)
        
        # Remove the directory from sys.path
        sys.path.pop(0)
    except Exception as e:
        print(f"Error importing module: {e}")
        return []
    
    # Find all Scene classes in the module
    scene_classes = []
    
    # Import manim Scene class
    try:
        from manim import Scene
        
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Scene) and obj != Scene:
                scene_classes.append(name)
                
    except ImportError:
        print("Error: Could not import manim.Scene. Make sure manim is installed.")
        return []
    
    return scene_classes

def render_scenes(file_path, quality="high", play=False, output_dir=None):
    """
    Render all Scene classes in the given Manim Python file using the Manim CLI.
    
    Args:
        file_path (str): Path to the Manim Python file
        quality (str): Quality flag for manim CLI ('l', 'm', 'h', 'p', 'k')
        play (bool): Whether to play animations after rendering
        output_dir (str, optional): Directory to save output files
    """
    # Map quality options to CLI flags
    quality_map = {
        "low": "l",
        "medium": "m",
        "high": "h",
        "production": "p",
        "4k": "k"
    }
    
    # Convert to CLI flag format
    quality_flag = quality_map.get(quality, quality)
    if len(quality_flag) > 1:
        print(f"Warning: Invalid quality '{quality}', using 'high' quality")
        quality_flag = "h"
    
    # Find all scene classes
    scene_classes = find_scene_classes(file_path)
    
    if not scene_classes:
        print("No Scene classes found in the file")
        return
    
    # Construct base command
    base_cmd = ["manim"]
    if play:
        base_cmd.append("-p")
    base_cmd.append(f"-q{quality_flag}")
    
    if output_dir:
        base_cmd.extend(["--output_dir", output_dir])
    
    base_cmd.append(file_path)
    
    # Render each scene
    print(f"Found {len(scene_classes)} scene(s) to render:")
    for i, scene_class in enumerate(scene_classes, 1):
        print(f"[{i}/{len(scene_classes)}] Rendering {scene_class}...")
        
        # Build the command for this scene
        cmd = base_cmd.copy()
        cmd.append(scene_class)
        
        # Run the command
        try:
            subprocess.run(cmd, check=True)
            print(f"✓ {scene_class} rendered successfully")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error rendering {scene_class}: {e}")
    
    print("\nRendering complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Render all Manim scenes in a file using the Manim CLI')
    parser.add_argument('file_path', help='Path to the Manim Python file')
    parser.add_argument('--quality', '-q', default='high', 
                        choices=['low', 'medium', 'high', 'production', '4k'],
                        help='Quality setting for rendering (defaults to high)')
    parser.add_argument('--play', '-p', action='store_true',
                        help='Play the animations after rendering')
    parser.add_argument('--output', '-o', help='Directory to save output files')
    
    args = parser.parse_args()
    render_scenes(args.file_path, args.quality, args.play, args.output)


# RUN AS 

# # Basic usage (renders all scenes at high quality)
# python manim_batch_cli.py your_file.py

# # With options
# python manim_batch_cli.py your_file.py --quality 4k --play