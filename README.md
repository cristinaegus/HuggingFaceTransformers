# Entorno Virtual para Hugging Face Transformers

Este entorno virtual está configurado específicamente para trabajar con la librería Transformers de Hugging Face y deep learning.

## Activar el entorno virtual

### En Windows PowerShell:

```powershell
.\venv_transformers\Scripts\Activate.ps1
```

### En Windows Command Prompt:

```cmd
venv_transformers\Scripts\activate.bat
```

## Librerías instaladas

- **transformers**: Librería principal de Hugging Face para modelos de transformers
- **torch**: PyTorch para deep learning
- **tensorflow**: TensorFlow para deep learning
- **numpy**: Computación numérica
- **pandas**: Manipulación de datos
- **matplotlib**: Visualización básica
- **seaborn**: Visualización estadística
- **scikit-learn**: Machine learning tradicional
- **jupyter**: Notebooks interactivos
- **ipykernel**: Kernel de Jupyter

## Uso en VS Code

El entorno virtual ha sido registrado como kernel de Jupyter con el nombre "Transformers HuggingFace". Para usarlo:

1. Abre un notebook (.ipynb) en VS Code
2. Haz clic en "Select Kernel" en la esquina superior derecha
3. Selecciona "Transformers HuggingFace" de la lista

## Instalación adicional de paquetes

Para instalar paquetes adicionales:

```powershell
# Activar el entorno
.\venv_transformers\Scripts\Activate.ps1

# Instalar paquete
pip install nombre_del_paquete
```

## Actualizar requirements.txt

Después de instalar nuevos paquetes:

```powershell
pip freeze > requirements.txt
```

## Recrear el entorno

Para recrear este entorno en otra máquina:

```powershell
# Crear nuevo entorno virtual
python -m venv venv_transformers

# Activar entorno
.\venv_transformers\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Registrar como kernel de Jupyter
python -m ipykernel install --user --name=venv_transformers --display-name="Transformers HuggingFace"
```

## ⚠️ Solución de Problemas

### Error de TensorFlow en Windows

Si encuentras errores relacionados con DLL de TensorFlow, este entorno está configurado para usar **solo PyTorch**:

- ✅ **PyTorch**: Completamente funcional
- ❌ **TensorFlow**: Deshabilitado por problemas de compatibilidad

#### Alternativas para usar TensorFlow:

1. **Google Colab** (recomendado)
2. **WSL (Windows Subsystem for Linux)**
3. **Docker con imagen de TensorFlow**

#### Variables de entorno configuradas:

```python
os.environ['USE_TF'] = 'NO'  # Usar solo PyTorch
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Deshabilitar optimizaciones oneDNN
```
