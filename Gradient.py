""" setting up initial variables """

import os
import numpy as np
import cv2

# getting the number of files in the directory that you choose, can also just manually change this value if you
# already know it but for computation in the rest of the program its useful to keep the DIR of all the images
DIR = '/Volumes/GoogleDrive/My Drive/CS Projects/GradientMaker/Edits'
total_images = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# set the dimensions of the final product you want
final_width = 21
final_height = 10

# to open the base gradient image and read its values as RGB
image = cv2.imread("/Volumes/GoogleDrive/My Drive/CS Projects/GradientMaker/Base.jpg")  # base is 480x270
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height = image.shape[0]  # 270
width = image.shape[1]  # 480
height_increment = int(height / final_height)
width_increment = int(width / final_width)
colour_goals = [[0 for x in range(final_width)] for y in range(final_height)]
x = 0
y = 0
print(height_increment, width_increment)
for i in range(final_height):
    x = height_increment * i
    for j in range(final_width):
        y = width_increment * j
        # print("i = {}, j = {}".format(i,j))
        # print("x = {}, y = {}".format(x,y))
        colour_goals[i][j] = image[x, y]
# print(colour_goals[5][7])


# list of all the filenames in the given directory
image_names = sorted(os.listdir(DIR))

# dictionary to store the dominant colours
dom_colour = {}

for name in image_names:
    print(DIR + '/' + name)
    image = cv2.imread(DIR + '/' + name)

    print(image_names.index(name))
    # resizing image to make it easier to work with and save computation time
    image = cv2.resize(image, (300,300) , interpolation=cv2.INTER_AREA)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixel_values = image.reshape((-1, 3))
    # convert to float
    pixel_values = np.float32(pixel_values)

    # define stopping criteria so that my computer doesnt explode
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    # number of clusters (K)
    k = 3

    # labels tells us which cluster we are looking at
    # we randomly assign the first set of clusters to ensure full accuracy
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # convert back to 8 bit values
    centers = np.uint8(centers)

    # flatten the labels array
    labels = labels.flatten()

    # convert all pixels to the color of the centroids
    segmented_image = centers[labels.flatten()]

    # storing the dominant colours of each of the images, in order of processing
    dom_colour[name] = segmented_image[0]
    # print(segmented_image[0])

print(dom_colour)

dom_colour ={'0021243437_10.jpg': [74, 42, 65], '070_shakeglitterEP-1.jpg': [58, 36, 65], '0d70e01x3d501.jpg': [ 67,  84, 163], '100000x100000-999.jpg': [254,  21, 122], '1276304.jpg': [152,  13,  23], '1280x1280 1).jpg': [216, 110,  54], '1280x1280 8).jpg': [239,  82,  77], '1280x12804).jpg': [125,  48,  31], '1329188.jpg': [219,   4,   5], '1500x1500sr.jpg': [254, 254, 254], '1504219747592.jpg': [103,  78, 106], '1604051142887-positionsalbum.jpg': [221, 212, 209], '176688d304aace4ffbcf9622cb6341ac.3000x3000x1.jpg': [10, 10, 10], '1997_DIANA-single4.jpg': [243, 243, 243], '1998 TRUMAN cover.jpg': [240, 237, 236], '1999-wildfire-brockhampton.jpg': [145, 144, 139], '2017+-+RAF.jpg': [230, 229, 228], '2019-11-22 08.46.00 1.jpg': [222, 191, 206], '2019-12-28 06.20.08 1.jpg': [169, 147, 143], '2020-03-07 12.39.49 1.jpg': [109, 121, 102], '2020-03-13 09.44.12 1.jpg': [216, 190, 189], '2020-05-04 11.19.37 1.jpg': [100, 100, 100], '20200709_155528.jpg': [235, 232, 230], '20200711_161725.jpg': [87, 70, 60], '20201220_172455.jpg': [20, 63, 76], '20201220_172459.jpg': [195,  20,  15], '20210310_022533.jpg': [212, 212, 213], '20210331_132353.jpg': [250, 250, 249], '20210427_171949.jpg': [144, 109,  79], '20210508_183618.jpg': [220, 218, 210], '26xfe7j8t0c51.jpg': [242, 183, 199], '2b5fe1c.jpg': [195, 159, 140], '2d7cf4b.jpg': [8, 7, 8], '2f5afe6.jpg': [219, 198, 208], '4.44 cover.jpg': [242, 193, 153], '41bd0a1.jpg': [222,  27,  55], '43cc85f.jpg': [254, 254, 254], '47bdbd8.jpg': [28, 29, 28], '4a7533d.jpg': [238,  33,  64], '4c1cc9a1).jpg': [206, 209, 223], '4c1cc9a.jpg': [222, 223, 222], '4c4834f.png': [51, 23, 22], '4d567c6.png': [253, 249, 248], '4d8e09b.png': [21, 80, 71], '5499c86.jpg': [64, 63, 67], '5b06f76488473_PUSHA-TDAYTONAFINAL_5b06f764b4f3d.jpg': [123, 109, 102], '5c468cceae5fce791c57888160926eda.1000x1000x1.jpg': [241, 237, 236], '5d14ca6.jpg': [213, 215, 213], '5de1eb79.jpg': [174, 206, 217], '5f49ebc.png': [238, 246, 246], '5fcd759.jpg': [245, 176, 192], '64c0c69.png': [223,  63,  57], '6532025.jpg': [200, 200, 200], '699c86f.jpg': [241,  78,  76], '69c1890.png': [223,  70,  93], '6dfa7cb.png': [63, 53, 47], '76b34e3.jpg': [206,  32,  39], '780aa18.png': [105,  83, 116], '791da04.jpg': [234, 234, 233], '79633663_135233001273282_2236357520032123350_n.jpg': [214, 205, 201], '798dda8.png': [ 84,  74, 153], '7a08046.jpg': [234, 140, 184], '808s.jpg': [194, 203, 202], '808s_POSTER_4.jpg': [208, 199, 198], '808s_POSTER_6.jpg': [196, 184, 187], '808s_POSTER_7.jpg': [200, 192, 194], '81d91fc.png': [153, 186, 188], '84a78870c472f12e3387b1fa9aaa9518.1000x1000x1.jpg': [34, 28, 35], '859b9af.jpg': [ 79,  29, 175], '8638b42.jpg': [171, 142, 115], '8769467.jpg': [219,   7,  12], '888d7ed.png': [181, 199, 213], '94718b8.jpg': [111, 151, 205], '95c3f0b.png': [0, 0, 0], '972e0db.jpg': [34, 33, 24], '9a929df.jpg': [220, 220, 220], 'B2wFydVCcAAM_sN.jpg': [227, 227, 227], 'CANNON cover.jpg': [154, 204,   5], 'CLOUT COBAIN cover.jpg': [245, 244, 244], 'COPx91uUAAAJLts.jpg': [204, 183, 181], 'Calvin-Harris-Slide-1500x1500.jpg': [244, 240, 242], 'Cayendo cover.jpg': [253, 233,   0], 'CdxmPB7UEAQkFgY.jpg': [121,   3,   8], 'Chance-the-Rapper-Coloring-Book.jpg': [247, 106, 110], 'CwY0fUIUoAAZjdV.jpg': [ 6, 10,  2], 'DHL cover.jpg': [  1, 125, 252], 'Darkest Before Dawn cover.jpg': [72, 72, 72], 'DcFNwlBU0AECQbO-1525185099-compressed.jpg': [216, 202, 176], 'DeBwLe2VAAAQ3en.jpg': [24, 24, 23], 'EB-l3DPUYAA4AAs.jpg': [144, 164, 172], 'EDOhpWiXsAUVczm.jpg': [145, 101,  90], 'EDuXNOfXUAA8jBe.jpg': [24, 19, 20], 'Frank-Ocean-Blonde-2016-2480x2480.jpg': [228, 230, 229], 'GINGER RADIO Episode 3 Cover 2.jpg': [252,  71,  70], 'HIGHEST IN THE ROOM cover.jpg': [ 65,  91, 134], 'IGOR.jpg': [238, 175, 194], 'Imperial cover.jpg': [161, 158, 140], 'In My Room cover.jpg': [220, 220, 220], 'MBDTF Cover.jpg': [236,  36,  64], 'MFTR_FINAL1-1500x1500.jpg': [57, 57, 57], 'PURPLE_FUTURE_COVER-1.jpg': [249, 247, 244], 'SATURATION III cover.jpg': [239, 246, 251], 'SATURATION cover.jpg': [251, 251, 251], 'Screenshot_20191226-202259.png': [234, 181, 197], 'Screenshot_20200114-064140.png': [203, 188, 186], 'THE-LIFE-OF-PABLO-2-KANYE-PDP-layered.jpg': [239, 136,  86], 'The-Slow-Rush.jpg': [78, 30, 17], 'TheWeeknd_HouseOfBalloons.jpg': [232, 232, 232], 'Troye-Sivan-Blue-Neighbourhood_2015-12-18_16-41-15.jpg': [ 59,  75, 102], 'Tyler_Alt_Bigger.jpg': [238, 134,  34], 'Webp.net-compress-image.jpg': [14, 29, 38], 'Wolves orange).jpg': [229, 142,  97], 'Yandhi-4096.jpg': [248, 245, 243], 'a1979723121_10.original.jpg': [137, 124, 118], 'a629763.jpg': [123, 200, 199], 'aap-forever-aap-rocky-feat-moby.jpg': [25, 14, 12], 'aaprocky_atlonglastaapdeluxee_cm7g.jpg': [13,  9,  8], 'aca7a0d.jpg': [ 74, 125, 159], 'aebbb37.jpg': [133,  69,  49], 'alternate cover.jpg': [231, 220, 189], 'ariana-grande-no-tears-left-to-cry-1571860504-compressed.jpg': [38, 29, 44], 'arianagrande_focussingle_cni6.jpg': [222, 207, 220], 'arianagrande_thankunextphysicalve_brvo.jpg': [19, 21, 20], 'b24ff18.jpg': [225, 229, 230], 'b786bad.jpg': [18,  7, 26], 'b890bf4.png': [236, 159, 135], 'bd6ed7d.jpg': [180, 137,  80], 'bigseanfeaturingcomm_switchupsingleexplic_622d.jpg': [ 12,  76, 180], 'bohemianlay_20201227_041544_0.jpg': [187,  59,  75], 'c08a48b.jpg': [ 72, 131, 181], 'censored cover.jpg': [205,  31,  51], 'ckigrzyq0mx51.jpg': [108,  98, 102], 'cover102).jpg': [47, 36, 47], 'cover103).jpg': [118,  55,  64], 'cover111).jpg': [11, 73, 80], 'cover116).jpg': [229, 229, 229], 'cover117).jpg': [ 74, 102, 151], 'cover121).jpg': [254, 254, 254], 'cover126).jpg': [224, 216, 199], 'cover127).jpg': [33, 30, 27], 'cover128).jpg': [163,  42,  16], 'cover131).jpg': [102,  13,  14], 'cover137).jpg': [249,  66,  67], 'cover138).jpg': [55, 52, 46], 'cover149).jpg': [238, 239, 237], 'cover15).jpg': [174,  97, 118], 'cover154).jpg': [109,  48, 102], 'cover16).jpg': [178,  51,  48], 'cover17).jpg': [240,  11,  12], 'cover178).jpg': [ 77, 122, 140], 'cover18).jpg': [35, 38, 36], 'cover183).jpg': [237, 198, 187], 'cover19).jpg': [93, 91, 91], 'cover22).jpg': [214, 158, 126], 'cover24).jpg': [251, 251, 252], 'cover26).jpg': [166, 147, 156], 'cover29).jpg': [242, 137,  84], 'cover34).jpg': [236, 110,   8], 'cover36).jpg': [  1,   5, 102], 'cover40).jpg': [18, 22,  7], 'cover41).jpg': [254, 254, 254], 'cover43).jpg': [235,  92,  80], 'cover47).jpg': [136, 122, 121], 'cover67).jpg': [8, 7, 6], 'cover68).jpg': [230, 214, 130], 'cover7).jpg': [40, 37, 40], 'cover74).jpg': [226, 135, 113], 'cover75).jpg': [111, 132, 153], 'cover77).jpg': [19, 19, 23], 'cover8).jpg': [241, 193, 191], 'cover82).jpg': [ 23,  49, 105], 'cover86).jpg': [231, 228, 222], 'cover87).jpg': [15, 27, 48], 'cover90).jpg': [168, 207, 218], 'cover91).jpg': [207, 202, 174], 'cover92).jpg': [232, 230, 230], 'deluxe edition cover2).jpg': [46,  9, 64], 'deluxe edition cover3).jpg': [74, 74, 74], 'deluxe edition cover.jpg': [29, 26,  9], 'drake_scorpion_axhm.jpg': [11, 11, 11], 'good kid.jpg': [215, 217, 217], 'iridescence alt cover.jpg': [ 14,  17, 112], 'kanye-808s.jpg': [203, 194, 199], 'kanyewest_mybeautifuldarktwist_2g1u.jpg': [206,  39,  63], 'kanyewest_runawaysingleexplici_cbd6.jpg': [ 51, 134, 116], 'kendricklamar_untitledunmasteredex_8g3r.jpg': [54, 55,  0], 'lil-yachty-lil-boat-3.jpg': [78, 16, 16], 'macmiller_thedivinefeminine_b4n8.jpg': [207, 186, 182], 'mchg_cover1.jpg': [13, 13, 13], 'moon river.jpg': [23, 19, 23], 'motm3.png': [ 97,  89, 181], 'nights.jpg': [6, 5, 6], 'nikes cover.jpg': [23, 36, 46], 'omf956loj3q21.jpg': [221, 205, 219], 'one.png': [249, 249, 249], 'onlyone-1.jpg': [15, 15, 15], 'pop 2 alt cover.jpg': [253, 252, 252], 'post_malone_rockstar_single_web.jpg': [40, 41, 38], 'provider cover.jpg': [161, 131, 137], 'sat2.jpg': [245, 246, 246], 'summertime-magic-childish-gambino.jpg': [36, 59, 92], 'theweeknd_echoesofsilence_41ln.jpg': [215, 221, 218], 'theweeknd_thursday_3lrf.jpg': [240, 238, 235], 'this-is-america.jpg': [179, 201, 206], 'tout.jpg': [254, 254, 254], 'troyesivan_bloomdeluxe_aupg.jpg': [13, 13, 13], 'troyesivan_bloomtargetdeluxeedi_b2ug.jpg': [33, 29, 28], 'ye.jpg': [201, 202, 206], 'z6kfwvvq9xqz.png': [29, 26, 28]}


# function to print numbers from one to ten
def print_numbers(n):
    for i in range(n):
        print(i+1)


# function to print numbers from ten to one
def print_numbers_backwards(n):
    for i in range(n):
        print(n-i)

print print_numbers(10)
print print_numbers_backwards(10)