import os
import shutil

src_images = "/Users/teddy/Library/CloudStorage/OneDrive-Personal/Documentos/Empresas/Impulsafit/Imagenes"
dst_images = "/Users/teddy/Library/CloudStorage/OneDrive-Personal/Documentos/Empresas/Impulsafit/src/assets/images"

src_logos = "/Users/teddy/Library/CloudStorage/OneDrive-Personal/Documentos/Empresas/Impulsafit/Logos"
dst_logos = "/Users/teddy/Library/CloudStorage/OneDrive-Personal/Documentos/Empresas/Impulsafit/src/assets/logos"

def copy_folder(src, dst):
    if not os.path.exists(src):
        print(f"Source folder not found: {src}")
        return
    if not os.path.exists(dst):
        os.makedirs(dst)
        print(f"Created destination directory: {dst}")
        
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            # Skip mov/mp4 files in src_images because we already optimized and wrote the video to public/videos/
            if item.lower().endswith(('.mov', '.mp4', '.avi')):
                print(f"Skipping video: {item}")
                continue
            shutil.copy2(src_path, dst_path)
            print(f"Copied {item} to {dst}")
        elif os.path.isdir(src_path):
            # Recursively copy if subdirs (none expected, but good practice)
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            print(f"Copied directory {item} to {dst}")

print("Copying images...")
copy_folder(src_images, dst_images)

print("\nCopying logos...")
copy_folder(src_logos, dst_logos)

print("\nDone copying assets!")
