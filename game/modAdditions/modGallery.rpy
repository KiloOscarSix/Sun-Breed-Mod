init python:
    import math
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = int(math.floor(len(filter(lambda s: s.char == char, galleryItems))/8)) + 1
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = os.path.join("/images/", "{}".format(thumbnail))
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    ## GALLERY ITEMS HERE
    GalleryItem("All", "galleryScene1", "/images/a53.webp")
    GalleryItem("All", "galleryScene2", "/images/a199.webp")
    GalleryItem("All", "galleryScene3", "/images/b168.webp")

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
    ["All", "/images/a186.webp"],
]

label galleryNameChange:
    default persistent.player_name = ""
    default persistent.rel_r2 = ""
    default persistent.rel_r = ""
    default persistent.rel_c = ""

    if not persistent.player_name:
        $ persistent.player_name = renpy.input("What is your name?")

    if not persistent.rel_r2:
        $ persistent.rel_r2 = renpy.input("Najah is your ??? Default will be friend.", default="friend").strip() or "friend"

    if not persistent.rel_r:
        $ persistent.rel_r = renpy.input("You are Najah's ??? Default will be friend.", default="friend").strip() or "friend"

    if not persistent.rel_c:
        $ persistent.rel_c = renpy.input("You both had the same ??? Default will be male caretaker.", default="male caretaker").strip() or "male caretaker"

    $ scopeDict = {"player_name":persistent.player_name, "rel_r2":persistent.rel_r2, "rel_r":persistent.rel_r, "rel_c":persistent.rel_c}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action Function(galleryDecreasePageNumber)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)