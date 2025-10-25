# style_going_wild
Create wildcards from your styles of SD Forge / A1111

This is a simple project with a huge impact, the simple script is creating exactly 2 .txt files from your custom styles you might have created using this function of Forge for Stable Diffusion.

<img width="372" height="183" alt="styleToWildcart2" src="https://github.com/user-attachments/assets/41dc3603-e793-435e-bfc3-4434379bd713" />

The Stand-Alone GUI Script (just start it) let you select a .csv file like your custom made style file from for ex. ..\webui_forge_cu124_torch24\webui\styles.csv

<img width="536" height="238" alt="style2wild_v2_img" src="https://github.com/user-attachments/assets/96ee91a2-c8f7-4b06-bde5-6634bee20f08" />

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

If you combine the wildcard with itself its also sometimes nice..

<img width="1191" height="605" alt="combined_styles" src="https://github.com/user-attachments/assets/9301ec43-02e4-47fc-b879-c1ff13116d45" />

(One of the original presets contain only a description of a cat but another preset (style) contains only the description of a grass field. The result is a random combination of both) with two random negative prompts).

<img width="423" height="251" alt="combined_styles2" src="https://github.com/user-attachments/assets/55f2ecde-62b6-4db6-8d8b-369a0db9e6f9" />

btw. a funny idea.. if you like strange monsters try to swap this vice versa. x-D

<img width="429" height="250" alt="sd_monsters" src="https://github.com/user-attachments/assets/fe852821-483e-42f2-a3dc-c1b1eabb089c" />

Known Bugs

- You might notice that there will be some errors in the console while the batch process starting procedure, this happens because some of the wildcard lines might have special signs like a $ character that could be missunderstud by the wildcard extension - just ignore that. I'm just creating a update with a additional checkbox to avoid this mostly.
- It might happen that a cascading effect will occupie because if you have a personal preset with a reference to __ my/01-prompt_styles __ for example your regular prompt reference to itself, in that cases its working but it could be that truly strange outputs you may sometimes get - also just ignore that.


Changelog

25.10.2025

- Added function to remove duplicated lines and empty lines
- Changed include buildin Styles checked as default
  
23.10.2025
- Added a option to correct each line for signs like "(", "[", "{".. -> Each line will be corrected if enabled (checked by default)
- Added a option to include the integrated styles file of forge as additional files
- New filename the filename of your own styles are now "01-prompt_styles.txt" and "02-negativ_styles.txt" (for the buildin styles_integrated.csv it is similar but with 03-.. and 04-..) the reason is to find them easier in your "my" directory.

<img width="442" height="239" alt="extended" src="https://github.com/user-attachments/assets/5db42eae-756d-44d5-a206-481469a2cd0d" />
