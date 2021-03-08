screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:
            textbutton _("Mod Options") action Show("modOptions")
            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    #code
    if main_menu:

        imagebutton idle "gui/start_idle.png" hover "gui/start_hover.png" focus_mask True action Start()

        imagebutton idle "gui/load_idle.png" hover "gui/load_hover.png" focus_mask True action ShowMenu("load")

        imagebutton idle "gui/option_idle.png" hover "gui/option_hover.png" focus_mask True action ShowMenu("preferences")

        imagebutton idle "gui/patreon_idle.png" hover "gui/patreon_hover.png" focus_mask True action OpenURL ("https://www.patreon.com/SuperWriter?fan_landing=true")

        imagebutton idle "gui/discord_idle.png" hover "gui/discord_hover.png" focus_mask True action OpenURL ("https://discord.gg/J227WNy")

        imagebutton idle "gui/logo_idle.png" hover "gui/logo_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        if renpy.variant("pc"):
            imagebutton idle "gui/quit_idle.png" hover "gui/quit_hover.png" focus_mask True action Quit(confirm=not main_menu)

        textbutton _("{size=100}Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")] align(1.0, 0.0)



    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
