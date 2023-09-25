import argparse
import glob
from PIL import Image
from functools import cmp_to_key

header = """
                              ,      \    /      ,
                             / \     )\__/(     / \\
                            /   \   (_\  /_)   /   \\
    _______________________/_____\___\@  @/___/_____\\____________________
   |                                 |\../|                              |
   |                                  \VV/                               |
   |   _______ _______  ______ _______  _____  _  _  _ _______ __   _    |
   |   |  |  | |_____| |_____/ |       |     | |  |  | |______ | \  |    |
   |   |  |  | |     | |    \_ |_____  |_____| |__|__| |______ |  \_|    |
   |_____________________________________________________________________|
     || ||               |    /\ /     \\\\     \ /\    |
     || ||               |  /   V       ))     V   \  |
     || ||               |/     `      //      '     \|
     || ||               `             V              '
    _||_||________________
   |                      |
   | FlipHTML5 IMG -> PDF |
   |______________________|
   """
print(header)
parser = argparse.ArgumentParser()
parser.add_argument("folderName", help="The folder containing images to be converted into pdf")
parser.add_argument("start", help="Starting image number to be converted", type=int)
parser.add_argument("end", help="Last image number to be converted", type=int)
args = parser.parse_args()
folderName = (args.folderName).strip("/")
start = args.start
end = args.end

print("Converting...")

images = []

def cmp(a, b):
    an = int(a.split('/')[1].split('.')[0])
    bn = int(b.split('/')[1].split('.')[0])

    if an < bn:
        return -1
    if an == bn:
        return 0
    if an > bn:
        return 1

for e in sorted(glob.glob(f"{folderName}/*.jpg"), key=cmp_to_key(cmp)):
    try:
        images.append(Image.open(e))
    except:
        pass

images[0].save("{0}.pdf".format(folderName), "PDF", resolution=100.0, save_all=True, append_images=images[1:])

print("\rFinished. Press any key to continue")
input()
