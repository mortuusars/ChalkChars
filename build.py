from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).parent
GENERATED = ROOT / "generated"
JAR = ROOT / "chalk-chars-1.0.0.jar"

INCLUDE = {
    Path("assets"),
    Path("data"),
    Path("META-INF"),
    Path("fabric.mod.json"),
    Path("icon.png"),
    Path("pack.mcmeta"),
}

# -- Copy generated files into the project

for source in GENERATED.rglob("*"):
    if source.is_file():
        target = ROOT / source.relative_to(GENERATED)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


# -- Create JAR

with zipfile.ZipFile(JAR, "w", zipfile.ZIP_DEFLATED, strict_timestamps=False) as jar:
    files = 0
    for path in INCLUDE:
        source = ROOT / path

        if source.is_file():
            jar.write(source, path)
            files += 1
        elif source.is_dir():
            for file in source.rglob("*"):
                if file.is_file():
                    relative = file.relative_to(ROOT)
                    jar.write(file, relative)
                    files += 1
    print(f"Written {files} files to jar: {str(JAR)}")


print(f"Created {JAR}")