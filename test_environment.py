#!/usr/bin/env python3
"""
Script de prueba para verificar el entorno de Hugging Face Transformers
"""
import os

# Configuración para usar solo PyTorch
os.environ['USE_TF'] = 'NO'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def test_transformers():
    """Prueba las funcionalidades básicas de transformers"""
    try:
        from transformers import pipeline
        print("✅ Transformers importado correctamente")
        
        # Prueba 1: Pipeline de sentiment analysis
        print("\n🔍 Probando pipeline de sentiment analysis...")
        classifier = pipeline("sentiment-analysis")
        result = classifier("I love using Hugging Face Transformers!")
        print(f"✅ Resultado: {result}")
        
        # Prueba 2: Importaciones adicionales
        print("\n📦 Verificando otras librerías...")
        import torch
        print(f"✅ PyTorch {torch.__version__}")
        
        import numpy as np
        print(f"✅ NumPy {np.__version__}")
        
        import pandas as pd
        print(f"✅ Pandas {pd.__version__}")
        
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Iniciando pruebas del entorno...")
    success = test_transformers()
    
    if success:
        print("\n🚀 El entorno está listo para usar!")
    else:
        print("\n⚠️ Hay problemas con el entorno.")
