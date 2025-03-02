#!/usr/bin/env python3
import os
import sys
import importlib.util
import inspect
from manim import Scene, config

def render_all_scenes(file_path, quality="1080p", output_dir=None):
    """
    Render all Scene classes in the given Manim file.
    
    Args:
        file_path (str): Path to the Manim Python file
        quality (str): Quality setting for rendering ('1080p', '4k', 'low_quality', 'medium_quality', 'high_quality')
        output_dir (str, optional): Directory to save output files
    """
    # Validate file path
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist")
        return
    
    if not file_path.endswith('.py'):
        print(f"Error: File '{file_path}' is not a Python file")
        return
    
    # Extract file information
    file_dir = os.path.dirname(os.path.abspath(file_path))
    file_name = os.path.basename(file_path)
    module_name = os.path.splitext(file_name)[0]
    
    # Set output directory
    if output_dir:
        config.output_dir = output_dir
    
    # Set quality
    if quality == "1080p":
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_rate = 60
        config.quality = "high_quality"  # Use Manim's expected quality string
    elif quality == "4k":
        config.pixel_height = 2160
        config.pixel_width = 3840
        config.frame_rate = 60
        config.quality = "fourk_quality"  # Use Manim's expected quality string
    elif quality in ["low_quality", "medium_quality", "high_quality", "production_quality", "fourk_quality", "example_quality"]:
        config.quality = quality
    else:
        print(f"Warning: Unknown quality '{quality}', using 1080p")
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_rate = 60
        config.quality = "high_quality"
    
    # Import the module
    try:
        # Create a spec from the file path
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        # Add the module to sys.modules to handle potential imports within the module
        sys.modules[module_name] = module
        # Execute the module
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Error importing module: {e}")
        return
    
    # Find all Scene classes in the module
    scene_classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, Scene) and obj != Scene:
            scene_classes.append((name, obj))
    
    if not scene_classes:
        print("No Scene classes found in the file")
        return
    
    # Render each scene
    print(f"Found {len(scene_classes)} scene(s) to render:")
    for i, (name, scene_class) in enumerate(scene_classes, 1):
        print(f"[{i}/{len(scene_classes)}] Rendering {name}...")
        try:
            scene = scene_class()
            scene.render()
            print(f"✓ {name} rendered successfully")
        except Exception as e:
            print(f"✗ Error rendering {name}: {e}")
    
    print("\nRendering complete!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Render all Manim scenes in a file')
    parser.add_argument('file_path', help='Path to the Manim Python file')
    parser.add_argument('--quality', '-q', default='1080p', 
                        choices=['1080p', '4k', 'low_quality', 'medium_quality', 'high_quality', 'production_quality', 'fourk_quality', 'example_quality'],
                        help='Quality setting for rendering (defaults to 1080p)')
    parser.add_argument('--output', '-o', help='Directory to save output files')
    
    args = parser.parse_args()
    render_all_scenes(args.file_path, args.quality, args.output)

# RUN IN CLI 
# python manim_batch_renderer.py animations.py --quality high_quality --output ./renders