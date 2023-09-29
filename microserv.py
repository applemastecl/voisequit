from flask import Flask, request, jsonify
from spleeter.separator import Separator
from pydub import AudioSegment
import os

app = Flask(__name__)

@app.route('/procesar-audio', methods=['POST'])
def procesar_audio():
    # Obtén el archivo de audio cargado por el usuario
    archivo = request.files['archivo']

    if archivo:
        # Guarda el archivo en el servidor
        archivo_path = os.path.join('uploads', archivo.filename)
        archivo.save(archivo_path)

        # Llama a tu función de procesamiento de audio
        instrumental_audio_paths = remove_vocals(archivo_path)

        # Combina los segmentos de audio en un archivo único
        combined_output_file = "instrumental_combined." + archivo.filename.split('.')[-1]
        combine_audio_segments(instrumental_audio_paths, combined_output_file)

        # Devuelve una respuesta JSON con la ubicación del archivo procesado
        response = {'archivo_procesado': combined_output_file}
        return jsonify(response)

    # Manejo de errores si no se proporciona un archivo
    return jsonify({'error': 'No se proporcionó ningún archivo'})

if __name__ == '__main__':
    app.run(debug=True)
