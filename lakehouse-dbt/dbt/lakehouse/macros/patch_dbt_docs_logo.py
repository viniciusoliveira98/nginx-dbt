import os
import shutil

# caminhos
target_dir = ".../dbt/lakehouse/target"
index_path = os.path.join(target_dir, "index.html")
logo_path = ".../dbt/lakehouse/target/images.png"
target_logo_path = os.path.join(target_dir, "images.png")

# read
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

#replace
content = content.replace('ng-src="{{ logo }}"', 'ng-src="images.png"')
content = content.replace('width: 100px', 'width: 150px')

#write
with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
    
print("✔️ Logo atualizado")