El objetivo de la pre-entrega de proyecto es aplicar los conocimientos adquiridos hasta la Clase 8 del curso, demostrando mi capacidad para automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python. Este proyecto me permitirá poner en práctica lo aprendido sobre interacción con elementos web, estrategias de localización y validación de estados en una página. El sitio objetivo para esta automatización será saucedemo.com, una aplicación web demo especialmente diseñada para prácticas de testing.

Para dicho proyecto estaremos utilizando python como lenguaje base, pytest para llevar a cabo los tests automatizados y selenium para poder interactuar con la página, que nos permitirá llevar a cabo los anteriormente mencionados tests automáticos.

Para instalar python utilicé el plugin "winget", el cual podes manipular a través del CMD ejecutando como administrador dicho programa.
winget install -e --id Python.Python.3.14
Instalación de pytest: (Usando el plugin pip que viene instalado por defecto, se puede acceder a él a través de cualquier terminal)
pip install pytest
Instalación de selenium webdriver: (Usando el anteriormente mencionado "pip")
pip install selenium