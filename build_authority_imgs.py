import subprocess, pathlib
SRC=pathlib.Path(r"C:/Users/conta/Downloads/TRABALHO/experts/helena morelo")
IMG=pathlib.Path("img")

# Helena photo -> square 320x320
subprocess.run(["ffmpeg","-v","error","-y","-i",str(SRC/"ChatGPT Image 8_09_2026, 11_36_55.png"),
  "-vf","scale=320:320:flags=lanczos","-c:v","libwebp","-quality","84",str(IMG/"helena.webp")],check=True)

# 6 client result photos -> crop to 1055:1491 ratio then 600w / 1000w
FILES=[f"ChatGPT Image 11_09_2026, 06_09_24 ({i}).png" for i in range(1,7)]
for i,fn in enumerate(FILES, start=1):
    src=str(SRC/fn)
    for tag,w,q in (("sm",600,76),("hd",1000,80)):
        out=str(IMG/f"cl{i}-{tag}.webp")
        subprocess.run(["ffmpeg","-v","error","-y","-i",src,
          "-vf",f"crop=992:1402:65:0,scale={w}:-2:flags=lanczos",
          "-c:v","libwebp","-quality",str(q),"-compression_level","6",out],check=True)
        print(f"cl{i}-{tag}", pathlib.Path(out).stat().st_size//1024,"KiB")
print("helena.webp", (IMG/"helena.webp").stat().st_size//1024,"KiB")
