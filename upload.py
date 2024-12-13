from flask import Flask, request, render_template_string
import os
import werkzeug.utils
import sys

app = Flask(__name__)

UPLOAD_FOLDER = sys.argv[1] if len(sys.argv) > 1 else 'uploads'
ALLOWED_EXTENSIONS = sys.argv[2].split(',') if len(sys.argv) > 2 else {'zip','py'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uploaded_ips = {}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    error_message = None
    client_ip = request.remote_addr  

    # Check if the client IP has already uploaded a file
    if client_ip in uploaded_ips and uploaded_ips[client_ip]:
        error_message = "You can only upload one file per IP address."
        return render_template_string(upload_form_template, error_message=error_message)

    if request.method == 'POST':
        # Check if the 'files' part is in the request
        if 'files' not in request.files:
            error_message = "No file part"
            return render_template_string(upload_form_template, error_message=error_message)

        files = request.files.getlist('files')  # Get the list of files
        
        if not files:
            error_message = "No selected file"
            return render_template_string(upload_form_template, error_message=error_message)

        for file in files:
            if file and allowed_file(file.filename):
                filename = werkzeug.utils.secure_filename(file.filename)
                name, extension = os.path.splitext(filename)
                new_filename = f"{name}_{client_ip}{extension}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            else:
                error_message = f"File type not allowed. Please upload only {', '.join(ALLOWED_EXTENSIONS)} files."
                return render_template_string(upload_form_template, error_message=error_message)
        uploaded_ips[client_ip] = True  # Mark the IP as having uploaded a file
        error_message = f"File(s) uploaded successfully."
        return render_template_string(upload_form_template, error_message=error_message)
    
    return render_template_string(upload_form_template, error_message=error_message)

upload_form_template = """
                        <!doctype html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Upload Files</title>
                            
                            <style>
                                @font-face {
                                    font-family: 'Font Awesome 6 Free';
                                    font-style: normal;
                                    font-weight: 900;
                                    src: url('fa-solid-900.woff2') format('woff2');
                                }
                                /* General styling */
                                body {
                                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                                    background-color: #f4f7fc;
                                    margin: 0;
                                    padding: 0;
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                    height: 100vh;
                                    color: #333;
                                }

                                /* Container styling */
                                .container {
                                    background: #fff;
                                    border-radius: 10px;
                                    padding: 30px;
                                    width: 400px;
                                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
                                    text-align: center;
                                }

                                /* Header styling */
                                h1 {
                                    font-size: 1.8rem;
                                    color: #0056b3;
                                    margin-bottom: 20px;
                                }

                                /* File input styling */
                                .file-upload {
                                    border: 2px dashed #ccc;
                                    background-color: #fafafa;
                                    padding: 20px;
                                    border-radius: 8px;
                                    cursor: pointer;
                                    text-align: center;
                                    transition: background-color 0.3s ease;
                                    margin: 20px 0;
                                }

                                .file-upload:hover {
                                    background-color: #e0f7fa;
                                }

                                .file-upload i {
                                    font-size: 3rem;
                                    color: #0056b3;
                                }

                                .file-upload p {
                                    font-size: 1.2rem;
                                    color: #555;
                                }

                                .file-list {
                                    margin-top: 15px;
                                    font-size: 1rem;
                                    color: #333;
                                    text-align: left;
                                }

                                /* Error alert box */
                                .alert {
                                    background-color: #f8d7da;
                                    color: #721c24;
                                    padding: 10px;
                                    border: 1px solid #f5c6cb;
                                    border-radius: 5px;
                                    margin-top: 15px;
                                    display: inline-block;
                                }

                                /* Submit button */
                                input[type="submit"] {
                                    padding: 12px 20px;
                                    font-size: 1.2rem;
                                    background-color: #0056b3;
                                    color: white;
                                    border: none;
                                    border-radius: 5px;
                                    cursor: pointer;
                                    width: 80%;
                                    transition: background-color 0.3s ease;
                                }

                                input[type="submit"]:hover {
                                    background-color: #00408d;
                                }

                            </style>
                        </head>
                        <body>

                        <div class="container">
                            <h1>Upload Files</h1>

                            {% if error_message %}
                                <div class="alert">{{ error_message }}</div>
                            {% endif %}

                            <form method="post" enctype="multipart/form-data">
                                <div id="drop-area" class="file-upload" ondrop="dropFile(event)" ondragover="allowDrop(event)" onclick="triggerFileInput()">
                                    <i class="fas fa-cloud-upload-alt"></i>
                                    <p>Drag and drop files here, or click to select</p>
                                    <em><span>Allowed file types: """ + ', '.join("." + ext for ext in ALLOWED_EXTENSIONS) + """</span></em>
                                    <input type="file" name="files" id="fileInput" style="display: none;" onchange="handleFileSelect(event)" multiple>
                                </div>
                                <div id="fileList" class="file-list"></div>
                                <input type="submit" value="Upload">
                            </form>
                        </div>

                        <script>
                            // Allow drop event
                            function allowDrop(event) {
                                event.preventDefault();
                                document.getElementById('drop-area').style.backgroundColor = '#e0f7fa';
                            }

                            // Handle drop event
                            function dropFile(event) {
                                event.preventDefault();
                                const fileInput = document.getElementById('fileInput');
                                const files = event.dataTransfer.files;
                                if (files.length > 0) {
                                    fileInput.files = files;
                                    displayFileList(files);
                                }
                            }

                            // Handle file selection through click
                            function handleFileSelect(event) {
                                const files = event.target.files;
                                displayFileList(files);
                            }

                            // Display list of selected or dropped files
                            function displayFileList(files) {
                                const fileListDiv = document.getElementById('fileList');
                                fileListDiv.innerHTML = ''; // Clear current file list
                                const fileNames = Array.from(files).map(file => `<li>${file.name}</li>`).join('');
                                fileListDiv.innerHTML = `<ul>${fileNames}</ul>`;
                            }

                            // Trigger the file input dialog when the drop-area is clicked
                            function triggerFileInput() {
                                document.getElementById('fileInput').click();
                            }

                            // Optional: Reset drop area styling when files are deselected
                            document.getElementById('fileInput').addEventListener('change', function() {
                                if (!this.files.length) {
                                    document.getElementById('drop-area').style.backgroundColor = '#fafafa';
                                    document.getElementById('fileList').innerHTML = '';
                                    document.getElementById('drop-area').innerHTML = `<i class="fas fa-cloud-upload-alt"></i><p>Drag and drop files here, or click to select</p>`;
                                }
                            });
                        </script>

                        </body>
                        </html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
