import os
import shutil
import argparse
from pathlib import Path

def copy_files(src, dest):
    try:
        if not os.path.exists(src):
            print(f"Dir does not exist: {src}")
            return
        
        os.makedirs(dest, exist_ok=True)
        
        for item in os.listdir(src):
            item_path = os.path.join(src, item)
            
            if os.path.isdir(item_path):
                copy_files(item_path, dest)
            else:
                extension = Path(item).suffix[1:]
                if not extension:
                    extension = 'no_extension'
                extension_dir = os.path.join(dest, extension)
                
                os.makedirs(extension_dir, exist_ok=True)
                
                shutil.copy(item_path, extension_dir)
                print(f"File {item} copied to {extension_dir}")
    
    except Exception as e:
        print(f"Error during directory processing: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy files to new directory and sort them.")
    parser.add_argument("source", type=str, help="Path to the source directory.")
    parser.add_argument("destination", type=str, nargs='?', default="dist", help="Path to the dist directory.")

    args = parser.parse_args()

    copy_files(args.source, args.destination)

if __name__ == '__main__':
    main()