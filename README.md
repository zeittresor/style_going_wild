# style_going_wild
Create wildcards from your styles of SD Forge / A1111

This is a simple project with a huge impact, the simple script is creating exactly 2 .txt files from your custom styles you might have created using this function of Forge for Stable Diffusion.

<img width="372" height="183" alt="styleToWildcart2" src="https://github.com/user-attachments/assets/41dc3603-e793-435e-bfc3-4434379bd713" />

The Stand-Alone GUI Script (just start it) let you select a .csv file like your custom made style file from for ex. ..\webui_forge_cu124_torch24\webui\styles.csv

<img width="495" height="221" alt="styleToWildcart3" src="https://github.com/user-attachments/assets/de04fabe-61be-4cc7-9d01-060878399303" />

If you select this file and click the "Generate" button an new folder will be created called "Generated_Styles" (in the same folder where the script is).

-> Now you can left the GUI Script.
-> Copy both newly created files "prompt_styles.txt" and "negativ_styles.txt" to the following folders (if you dont have both extensions might be enough to use one of this):

"..\webui_forge_cu124_torch24\webui\extensions\stable-diffusion-webui-wildcards\wildcards\my" (if you dont have a "my" folder there just create / use it)

"..\webui_forge_cu124_torch24\webui\extensions\sd-dynamic-prompts\wildcards\my" (..same procedure here)

Now start (or better "restart" SD Forge WebUI). Set your Batch to the max (usual the max is 100 but you could change it in your user settings json file for ex. to 2500 in the "..\webui_forge_cu124_torch24\webui" folder if you like).

Now you can select both Wildcards from the Wildcard Tab (if you dont have it try to enter this in the prompt field: __my/prompt_styles__ in the negative prompt filed you might want to enter __my/negativ_styles__

<img width="429" height="250" alt="styleToWildcart" src="https://github.com/user-attachments/assets/987e7510-1fc9-4214-9671-136a162fff2c" />

Now click generate and wait / sleep / what ever.. (it might take some time to start because a style as a wildcard needs much more time for the "Start" (but not for the generation process if you use the batch function.)

If you come back some times later you might find a lot new images in different combined styles and combined with the different negative styled you have entered once for a specific prompt but now for a different one. ;-)

You can also double or combine the prompt and negative prompt or enter it twice or more for quadrillions of different style images.. 

A funny idea.. if you like strange monsters try to swap this o_O x-D

<img width="429" height="250" alt="sd_monsters" src="https://github.com/user-attachments/assets/fe852821-483e-42f2-a3dc-c1b1eabb089c" />
