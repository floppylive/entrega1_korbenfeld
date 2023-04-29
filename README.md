# proyecto-django

Para acceder a la funcionalidad debe hacer:

Contiene los modelos: Aviso Usuario Frase

Se está creando un boceto de lo que va a ser la página de frases. La página tiene la posibilidad de generar frases de manera anónima y los admins pueden o no deshabilitar la frase si la consideran indebida. A futuro, sólo los que tengan usuario podrán ver las frases en estado privado. Mientras tanto, al público sólo se puede mostrar las frases en público en la sección "buscar frase". Por ahora, ya que la página está en estado de pruebas cualquiera puede registrarse como usuario .

Se puede: Crear usuario Crear aviso Buscar palabra clave para encontrar las frases Está la función buscar usuario pero no se hizo pública la implementación.

Para correr la página debe migrarse y ejecutar el servidor

-python manage.py migrate -python manage.py runserver