# recipebot
# Programa Python para crear un bot de recetas en Twitter/X.com
![ejemplo](https://github.com/user-attachments/assets/06d3f7a2-c4ce-41d3-a277-60738ae1df69)

## Tutorial para las claves
1. Entrar a twitter developer -> developer portal
2. Crear una aplicación
3. En configuración de la aplicación, apartado Keys and Tokens, genera las siguientes claves. Es importante que no las compartas con nadie:
   ![keys](https://github.com/user-attachments/assets/93a7668a-e8d8-45e6-a064-8d85b362c3f9)
4. Clona el repositorio y rellena el apartado de claves del código con las que has obtenido para tu aplicación:
   ![claves](https://github.com/user-attachments/assets/d9e789cf-09f2-4f15-98ba-8831df3b158f)

## Conceder permisos de escritura a la aplicación
1. En el portal de desarrolladores, en la configuración de la aplicación, accede al apartado User authentication settings
  ![user_autentication_settings](https://github.com/user-attachments/assets/fff555cc-6687-4326-b612-76e06bc8ac8e)
2. Concede permisos de lectura y escritura:
  ![readandwrite](https://github.com/user-attachments/assets/240726e6-3658-49ea-afe2-26953d557e31)

## Tutorial para obtener el csv
El csv contendrá todos los registros de recetas a los que accederá el bot, escogiendo un registro cada día. Debemos acceder a Kaggle y registrarnos.
1. Accede a [Recipe Dataset (over 2M) Food](https://www.kaggle.com/datasets/wilmerarltstrmberg/recipe-dataset-over-2m)
2. Descarga el dataset
3. Especifica en el código en qué directorio has almacenado el dataset:
  ![dataset](https://github.com/user-attachments/assets/6c2e57ad-df28-435f-a5e2-8d0861cd516f)

## Tutorial para etiqueta Automated en Twitter
Según la normativa actual de Twitter/X, debemos especificar cuándo una cuenta es un bot (realiza publicaciones automatizadas). Para ello es necesario tener dos cuentas, la aplicación del bot + una cuenta personal a la que vincular el bot.
1. Dentro de Twitter, accede a more/configuración ⚙️
2. Your account -> Automation
3. Vincula la cuenta del bot con la cuenta principal
4. Al acabar el proceso, revisa si ha funcionado visualizando la siguiente etiqueta en tu perfil:
  ![label](https://github.com/user-attachments/assets/348ab351-b963-4a60-9e7e-1d483f91027b)
