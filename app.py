from flask import Flask, request, render_template
from filter import generate_line_with_keywords
from Main import make_api_call
from converter import generate_mermaid_code
from trial import generate_html_with_mermaid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        textarea_content = request.form['textarea_content']
        
        # Generate the line with keywords
        line_with_keywords = generate_line_with_keywords(textarea_content)
        print("Line with Keywords:", line_with_keywords)
        
        # Make API call
        api_response = make_api_call(line_with_keywords)
        print(api_response)

        mermaid = generate_mermaid_code(api_response)
        print(mermaid)

        output = generate_html_with_mermaid(mermaid)
        


        
        return output
    
    return render_template('interface.html')

if __name__ == '__main__':
    app.run(debug=True)
