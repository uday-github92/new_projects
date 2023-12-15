import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/point_cloud')
def serve_point_cloud():
    # Load the point cloud file
    cloud = pv.read('path/to/point_cloud_file.ply')

    # Save the point cloud as a temporary file
    tmp_file = 'temp_point_cloud.ply'
    cloud.save(tmp_file)

    # Return the point cloud file as a response
    return send_file(tmp_file, as_attachment=True)


@app.route('/mesh')
def serve_mesh():
    # Load the mesh file
    mesh = pv.read('path/to/mesh_file.obj')

    # Save the mesh as a temporary file
    tmp_file = 'temp_mesh.obj'
    mesh.save(tmp_file)

    # Return the mesh file as a response
    return send_file(tmp_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

