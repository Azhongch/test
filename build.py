import json
import os
import sys
from jinja2 import Template, exceptions

def build_resume():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'resume_data.json')
    template_path = os.path.join(base_dir, 'template.html')
    output_path = os.path.join(base_dir, 'index.html')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            resume_data = json.load(f)
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template_source = f.read()

        template = Template(template_source)
        html_output = template.render(data=resume_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)
            
        print("✅ Successfully built index.html")
        
    except exceptions.TemplateSyntaxError as e:
        print(f"❌ Template Syntax Error at line {e.lineno}: {e.message}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Build failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    build_resume()