import os, signal, subprocess
import time

def startADB():
    from adb import adb_commands
    from adb import sign_cryptography

    signer = sign_cryptography.CryptographySigner(
        op.expanduser('~/.android/adbkey'))

    device = adb_commands.AdbCommands()
    device.ConnectDevice(rsa_keys=[signer])

    return device



def capture_Screenshot( filename ):

    cmd = "adb exec-out screencap -p > {}".format(filename)
    pipe = subprocess.Popen(cmd,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
    pipe.wait()
    #os.killpg(os.getpgid(pipe.pid), signal.SIGTERM)  

def crop_picture( img_in ):
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop
    from PIL import Image 

    # Define the names
    imageFile_in = img_in
    imageFile_out= "out_" + img_in

    # Open the File 
    im = Image.open( imageFile_in )


    #/dev/input/event4: EV_ABS       ABS_MT_POSITION_X    0000000d = 13
    #/dev/input/event4: EV_ABS       ABS_MT_POSITION_Y    0000068d = 1677
    #/dev/input/event4: EV_ABS       ABS_MT_POSITION_X    000002df = 735
    #/dev/input/event4: EV_ABS       ABS_MT_POSITION_Y    00000779 = 1913

    # The crop method from the Image module takes four coordinates as input.
    # The right can also be represented as (left+width)
    # and lower can be represented as (upper+height).
    im_cropped = im.crop((13, 1677, 735, 1913))

    im_cropped.save(imageFile_out, quality=80)
    return imageFile_out


def compare_images( img1, img2, SSIM_FACTOR=0.8 ):
    from skimage.metrics import structural_similarity as ssim
    import cv2    # opencv-python

    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    imageA = cv2.imread( img1 )
    image_A = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

    imageB = cv2.imread( img2 )
    image_B = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    ### Structural Similarity Measure
    s = ssim(image_A, image_B)
    print("SSIM(x,y) = " + str(s))
    
    if s > SSIM_FACTOR:
        return True
    else:
        return False


def click_TryAgain():
    #subprocess.call("adb shell input tap 186 1802", shell = True)
    subprocess.call("adb shell input touchscreen swipe 186 1802 186 1802 5", shell = True)



###########

while(True):
    fileA1 = "sinoalice.png"
#    click_TryAgain()
#    time.sleep(30)

    print("Captures Screenshot")
    capture_Screenshot( fileA1 )


    print("Crop Screenshot")
    fileA2 = crop_picture( fileA1 )


    print("Compare Images")
    boolComp = compare_images( fileA2, "sinoalice_Try_Again.png", SSIM_FACTOR=0.7 )


    if boolComp == True:
        print("Click and Go ##")
        click_TryAgain()

    print("Sleep")
    time.sleep(15)

    print("\n")
