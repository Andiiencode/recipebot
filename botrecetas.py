import pandas as pd # lee los archivos csv
import tweepy # conecta con la api de twitter
import random # escoge encabezados random
import schedule # publicaciones periódicas
import time

# Localización del csv: Recipe Dataset (over 2M) Food
csv_kaggle = ''

# Credenciales necesarias de la API de Twitter v2
#API Key and Secret 
api_key = ''
api_secret = ''
#Access Token and Secret
access_token = ''
access_token_secret = ''
#Bearer Token
bearer_token = ''

# Inicializar cliente de Twitter
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#ARRAYS RANDOM 

# Array de encabezados para los tweets
encabezados = [
    "Tomorrow you can prepare:",
    "The food for tomorrow:",
    "Thinking about food? Try:",
    "Culinary surprise of the day!:",
    "How about cooking this today?:",
    "Meal idea for today:",
    "Quick recipe for today:",
    "Feeling hungry? Try this:",
    "Today’s perfect dish:",
    "Inspired to cook? Here's an idea:",
    "What’s cooking today? Try this:",
    "Need a meal idea? Here’s one:",
    "A delicious option for today:",
    "What’s for lunch? Try this:",
    "Craving something tasty? Cook this:",
    "Satisfy your hunger with this recipe:",
    "A must-try dish for today:",
    "Treat yourself with this meal:",
    "Today’s recipe recommendation:",
    "In the mood for something new? Cook this:",
    "Whip up something delicious today:",
    "Cook something special today:",
    "Your meal inspiration for the day:",
    "A recipe to brighten your day:",
    "Here you have an idea for tomorrow’s lunch:"
    "Feeling adventurous? Try cooking this:",
    "Dish of the day suggestion:",
    "New recipe to try today:",
    "Surprise your taste buds with this dish:",
    "Need a quick meal? Try this:",
    "A savory option for your table:",
    "Hungry for something new? Try this:",
    "Easy recipe for today’s meal:",
    "What’s on your menu today? Consider this:",
    "Can’t decide what to cook? Here's an idea:",
    "Elevate your cooking with this recipe:",
    "A tasty treat for today’s menu:",
    "Simple yet delicious: cook this today:",
    "A flavorful option for your day:",
    "What’s on today’s plate? Try this:",
    "Perfect recipe for today’s cravings:",
    "Cook up something fresh today:",
    "A dish to brighten your day:",
    "Feeling creative? Make this today:",
    "Quick and tasty idea for your meal:",
    "Fresh and easy recipe for today:",
    "Try this delightful dish today:",
    "Discover a new flavor today:",
    "Cook something memorable today:",
    "Time to eat? Try this recipe:",
    "Spice up your day with this dish:",
    "Healthy and delicious option for today:",
    "Today’s meal inspiration awaits:"
]

# Array emoji 
lista_emojis = [
        "🍜","🍝","🌮","🍿","🍗","🍖","🥪",
        "🥗","🍱","🍛","🌯","✨","✨","✨","✨","✨"
    ]

#Array de frase compras
frase_ingredientes = [
    "Ingredients:",
    "Things you need to buy:",
    "Grocery list:",
    "Items you'll need:",
    "What you'll need:",
    "Recipe components:",
    "Necessary ingredients:",
    "Shopping list:",
    "Ingredients list:",
    "What to gather:",
    "Required items:",
    "Food items:",
    "Kitchen essentials:",
    "Ingredient list:",
    "Stuff you need:",
    "Supplies for the recipe:",
    "Cooking necessities:",
    "Ingredients for this dish:",
    "What’s needed:",
    "Recipe ingredients:",
]

#Array para hashtags
hashtags = ["#Recipe", "#Food", "#FoodIdeas", "#Tasty", "#Foodie", "#HealthyFood", "#DailyFood"]

# Cargar el dataset desde un archivo CSV
def cargar_datos():
    ruta_archivo = csv_kaggle  
    datos = pd.read_csv(ruta_archivo)
    return datos[['title', 'NER']].dropna()  # Verifica que las columnas title y NER existen y no son null

# Función para seleccionar recetas aleatorias del dataset
def generar_array_comidas():
    try:
        datos = cargar_datos()
        if datos.empty:
            print("No se encontraron recetas en el dataset")
            return []
        
        comidas = []
        for _, row in datos.iterrows():
            comidas.append((row['title'], row['NER'])) #Recogemos título de la comida + ingredientes (NER)
        
        return comidas  # Devolver todas las recetas
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")
        return []

# Función para publicar el tweet
def publicar_tweet(mensaje):
    try:
        response = client.create_tweet(text=mensaje)
        print("Tweet publicado con éxito.")
        print("ID del tweet:", response.data['id'])
    except tweepy.TweepyException as e:
        print(f"Error al publicar el tweet: {e}")

# Función principal que ejecuta la tarea
def tarea_prueba():
    print("Ejecutando tarea de prueba con datos de Kaggle...")
    comidas = generar_array_comidas()  # Llama a la función que genera las comidas
    if comidas:
        titulo, ingredientes = random.choice(comidas)  # Receta random del array de comidas
        encabezado_random = random.choice(encabezados) # Encabezado random
        texto_ingredientes_random = random.choice(frase_ingredientes) # Texto random
        emoji_random = random.choice(lista_emojis) #Emoji random
        #Composición del mensaje
        mensaje = f"{emoji_random}{encabezado_random}\n{titulo}\n 🛒{texto_ingredientes_random}\n {', '.join(eval(ingredientes))}\n{' '.join(hashtags)}"
        print(f"Mensaje generado: {mensaje}")
        publicar_tweet(mensaje)
    else:
        print("No se pudo generar ninguna receta.")

# Programar para que se ejecute cada minuto (para realizar pruebas) = every(1)
# Para ejecutarlo cada día schedule.every().day.at("HH:MM").do(tarea_prueba)
print("Programando tarea para ejecutarse cada minuto...")
schedule.every().day.at("18:00").do(tarea_prueba)

print("Iniciando el bucle principal...")
while True:
    schedule.run_pending()
    print("Esperando la siguiente ejecución...")
    time.sleep(60)  # Espera un minuto antes de revisar otra vez
