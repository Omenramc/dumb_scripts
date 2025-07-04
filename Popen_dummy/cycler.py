import subprocess

def ejecutor(nombre):
    return subprocess.Popen(["python3", f"{nombre}"])

if __name__ == "__main__":
    uno = ejecutor("dummycycle1.py")
    dos = ejecutor("dummycycle2.py")
    try:
        uno.wait()
        dos.wait()
    except KeyboardInterrupt:
        uno.terminate()
        dos.terminate()
