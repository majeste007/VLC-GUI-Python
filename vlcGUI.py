from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image

app = Tk()
app.title("Lecteur multimedia VLC")
app.minsize(400,50)
app.iconbitmap("icones/favicon.ico")
h = app.winfo_screenheight()
w = app.winfo_screenwidth()

# création du menu genre la barre quoi
menu = Menu(app)

# création des menus
media_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Media", menu=media_menu)
# Ajouter des éléments de menu au menu Media
media_menu.add_command(label="Ouvrir un fichier")
media_menu.add_command(label="ouvrir plusieurs fichiers")
media_menu.add_command(label="Ouvrir un dossier")
media_menu.add_command(label="Ouvrir disque")
media_menu.add_command(label="Ouvrir un flux réseau")
media_menu.add_command(label="Ouvrir un periphérique de capture ")
media_menu.add_command(label="Ouvrir un emplacement depuis le papier presse")
media_menu.add_separator()
media_menu.add_command(label="Enregistrer la liste de lecture")
media_menu.add_command(label="Convertir/Enregistrer")
media_menu.add_command(label="Diffuser")
media_menu.add_separator()
media_menu.add_command(label="Quitter à la fin de la liste de lecture")
media_menu.add_command(label="Quitter", command=app.quit)


# lecture
read_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Lecture", menu=read_menu)
read_menu.add_command(label="Titre", state="disabled")
read_menu.add_command(label="Chapitre", state="disabled")
read_menu.add_command(label="Programme", state="disabled")
read_menu.add_command(label="Signets Personnalisés", state="disabled")
read_menu.add_separator()
read_menu.add_command(label="Rendu")
read_menu.add_separator()
read_menu.add_command(label="Vitesse ",state="disabled")
read_menu.add_separator()
read_menu.add_command(label="Avancer",state="disabled")
read_menu.add_command(label="Reculer",state="disabled")
read_menu.add_command(label="Aller à un temps spécifié")
read_menu.add_separator()
read_menu.add_command(label="Lire")
read_menu.add_command(label="Arrêter",state="disabled")
read_menu.add_command(label="Précédent",state="disabled")
read_menu.add_command(label="Suivant",state="disabled")
read_menu.add_command(label="Enregistrer",state="disabled")



# audio
audio_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Audio", menu=audio_menu)
audio_menu.add_command(label="Piste audio",state="disabled")
audio_menu.add_command(label="Périphérique audio")
audio_menu.add_command(label="Mode stéréo",state="disabled")
audio_menu.add_separator()
audio_menu.add_command(label="Visualisation",state="disabled")
audio_menu.add_separator()
audio_menu.add_command(label="Augmenter le volume")
audio_menu.add_command(label="Diminuer le volume")
audio_menu.add_command(label="Couper le son")


video_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Vidéo", menu=video_menu)
video_menu.add_command(label="Piste video",state="disabled")
video_menu.add_separator()
video_menu.add_command(label="Plein écran")
video_menu.add_command(label="Toujours adapter à la fenêtre",state="disabled")
video_menu.add_command(label="Definir comme papier peint")
video_menu.add_separator()
video_menu.add_command(label="Zoom",state="disabled")
video_menu.add_command(label="Rapport de cadre",state="disabled")
video_menu.add_command(label="Rogner",state="disabled")
video_menu.add_separator()
video_menu.add_command(label="Desentrelacer",state="disabled")
video_menu.add_command(label="Mode Desentrelacement",state="disabled")
video_menu.add_separator()
video_menu.add_command(label="Prendre un capture d'écran",state="disabled")

subtitle_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Sous-titre", menu=subtitle_menu)
subtitle_menu.add_command(label="Ajouter un fichier de sous titres")
subtitle_menu.add_command(label="Piste de sous-titres",state="disabled")

tools_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Outils", menu=tools_menu)
tools_menu.add_command(label="Effets et Filtres")
tools_menu.add_command(label="Synchronisation des pistes")
tools_menu.add_command(label="Informations sur le médio")
tools_menu.add_command(label="Informations sur le codecs")
tools_menu.add_command(label="Configuration VLM")
tools_menu.add_command(label="Guides des programmes")
tools_menu.add_command(label="Messages")
tools_menu.add_command(label="Extensions et greffons")
tools_menu.add_separator()
tools_menu.add_command(label="Personnaliser l'interfaces")
tools_menu.add_command(label="Preferences")

view_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Vue", menu=view_menu)
view_menu.add_command(label="Listes de lecture")
view_menu.add_checkbutton(label="Liste de lecture integrée")
view_menu.add_separator()
view_menu.add_command(label="Toujours au dessus")
view_menu.add_separator()
view_menu.add_command(label="Interface minimales")
view_menu.add_command(label="Interfaces plein écran")
view_menu.add_command(label="Controle avancés")
view_menu.add_command(label="Barre d'état")
view_menu.add_separator()
view_menu.add_command(label="Ajouter une interface")
view_menu.add_command(label="VLsub")

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Aide", menu=help_menu)
help_menu.add_command(label="Aide ")
help_menu.add_command(label="Verifié les mises à jour")
help_menu.add_separator()
help_menu.add_command(label="A propos")

# Frame principale
main_frame = Frame(app,background="#111" )
main_frame.place(x=0, y=0, height=h, width=w)
logo_get = Image.open("icones/vlc-48.png")
logo_resized = logo_get.resize([100,100])
logo = ImageTk.PhotoImage(logo_resized)
logo_vlc = Label(main_frame, image=logo)
logo_vlc.place(x=main_frame.winfo_width()*0.5, y=main_frame.winfo_height()*0.5)

app.config(menu=menu)
app.mainloop()