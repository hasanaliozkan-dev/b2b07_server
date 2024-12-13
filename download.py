from flask import Flask, send_from_directory #3.1.0
import os
import sys 


app = Flask(__name__)

folder_name = sys.argv[1]


EXAMPLE_FOLDER = folder_name  
ALLOWED_EXTENSIONS = {'py' , 'zip'}  



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():

    files = [f for f in os.listdir(EXAMPLE_FOLDER) if allowed_file(f)]
    

    html_content = """<!doctype html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">

            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
            <title>Available Files for Download</title>

            <style>
                @font-face {
                    font-family: 'Font Awesome 6 Free';
                    font-style: normal;
                    font-weight: 900;
                    src: url('fa-solid-900.woff2') format('woff2');
                }
                /* General styling */
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }

                /* Header */
                h1 {
                    text-align: center;
                    color: #0056b3;
                    margin-top: 20px;
                    font-size: 2rem;
                }

                /* Container for the file list */
                .container {
                    max-width: 800px;
                    margin: 20px auto;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                }

                /* List styling */
                ul {
                    list-style-type: none;
                    padding: 0;
                }

                ul li {
                    padding: 10px;
                    margin: 8px 0;
                    background: #e9f5ff;
                    border: 1px solid #d0e8ff;
                    border-radius: 6px;
                    transition: transform 0.2s ease, background-color 0.2s ease;
                }

                ul li a {
                    display: flex; /* Use flexbox to arrange name and icon */
                    justify-content: space-between; /* Space between name and icon */
                    align-items: center; /* Vertically align text and icon */
                    padding: 10px;
                    background: #e9f5ff;
                    border: 1px solid #d0e8ff;
                    border-radius: 6px;
                    text-decoration: none;
                    color: #0056b3;
                    font-size: 1rem;
                    font-weight: bold;
                    transition: transform 0.2s ease, background-color 0.2s ease;
                }
                ul li:hover {
                    background-color: #cfe6ff;
                    transform: scale(1.02);
                }
                ul li a .icon {
                    font-size: 1.2rem; /* Adjust icon size */
                    color: #0056b3;
                }

                /* Footer */
                footer {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
            </head>
            <body>
            <h1>Available Files for Download</h1>
            <div class="container">
            <ul>"""
    
    for file in files:
        html_content += f"""
                              <li>
                              <a href="/download/{file}" download>
                                    {file}
                                    <span class="icon"><i class="fas fa-download"></i></span>
                                </a></li>
                            
                        """
        
    
    html_content += '</ul>'
    
    return html_content

@app.route('/download/<filename>')
def download_file(filename):

    if allowed_file(filename) and os.path.isfile(os.path.join(EXAMPLE_FOLDER, filename)):
        return send_from_directory(EXAMPLE_FOLDER, filename, as_attachment=True)
    else:
        return "File not found or invalid file type", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
