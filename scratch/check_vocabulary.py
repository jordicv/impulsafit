import os
import re

search_dir = "/Users/teddy/Library/CloudStorage/OneDrive-Personal/Documentos/Empresas/Impulsafit/src"

prohibited_words = [
    r'\bclases\b',
    r'\bcupos\b',
    r'\binscribirse\b',
    r'\bven a entrenar\b'
]

# We need to check if any of these are present in .astro files
print("Checking for prohibited words in .astro source files...")
errors_found = 0

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.astro'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern in prohibited_words:
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                if matches:
                    errors_found += len(matches)
                    print(f"Error: Found prohibited pattern '{pattern}' in {file_path}:")
                    for m in matches:
                        start = max(0, m.start() - 30)
                        end = min(len(content), m.end() + 30)
                        snippet = content[start:end].replace('\n', ' ')
                        print(f"  Snippet: '...{snippet}...'")

if errors_found == 0:
    print("Success: No prohibited words found in the codebase!")
else:
    print(f"Failed: Found {errors_found} prohibited word occurrences.")
