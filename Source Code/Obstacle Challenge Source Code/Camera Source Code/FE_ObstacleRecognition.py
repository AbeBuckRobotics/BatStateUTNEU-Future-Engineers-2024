import sensor, time
from micropython import const
from pupremote import PUPRemoteSensor

camera = PUPRemoteSensor(power = True)
camera.add_channel('blob', to_hub_fmt = 'hhhhhh')

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 1000)
sensor.set_vflip(True)
sensor.set_hmirror(True)
clock = time.clock()

screenWidth = sensor.width()
screenHeight = sensor.height()
roiX= int(0.0 * screenWidth)
roiY = int(0.3 * screenHeight)
roiWidth = screenWidth - roiX * 2
roiHeight = screenHeight - roiY
roi = (roiX, roiY, roiWidth, roiHeight)

sensor.set_windowing(roi)
sensor.set_framerate(15)
# to consume less power

contestMode = False

_GREEN = const((0, 100, -128, -10, 20, 127))
_RED = const((0, 100, 7, 127, -10, 127))
# format: (Lmin, Lmax, Amin, Amax, Bmin, Bmax)

while True:
    img = sensor.snapshot()

    gBlobs = img.find_blobs([_GREEN], pixels_threshold = 400)
    gBlob, gPix, gCx, gCy = None, 0, 0, 0

    for g in gBlobs:
        if ((g.h() > g.w() or (g.y() + g.h()) == roiHeight) and g.pixels() > gPix):
            gPix = g.pixels()
            gBlob = g

    if (gBlob != None):
        gDen = gBlob.density()
        gCx = gBlob.cx()
        gCy = gBlob.cy()

        img.draw_rectangle(gBlob.rect(), (238, 39, 55), 1)

    rBlobs = img.find_blobs([_RED], pixels_threshold = 400)
    rBlob, rPix, rCx, rCy = None, 0, 0, 0

    for r in rBlobs:
        if (r.pixels() > rPix):
            rPix = r.pixels()
            rBlob = r

    if (rBlob != None):
        rCx = rBlob.cx()
        rCy = rBlob.cy()
        img.draw_rectangle(rBlob.rect(), color = (68, 214, 44), thickness = 1)

    print(gPix, rPix)
    camera.update_channel('blob', gCx, gCy, gPix, rCx, rCy, rPix)
    camera.process()
