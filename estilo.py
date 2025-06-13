from IPython.core.display import HTML

def set_custom_style():
    styles = """
    <style>
        .rendered_html {
            font-family: 'Fira Sans', 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.7;
            color: #2a2a2a;
            background-color: #f9fdfa;
            padding: 15px;
            border-radius: 10px;
        }
        h1 {
            color: #009688;
            font-weight: 700;
            border-bottom: 3px solid #009688;
            padding-bottom: 6px;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        h2 {
            color: #00796B;
            font-weight: 600;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        h3 {
            color: #004D40;
            font-weight: 500;
            margin-top: 25px;
            margin-bottom: 12px;
        }
        code {
            background-color: #e0f2f1;
            padding: 3px 7px;
            border-radius: 5px;
            font-family: 'Fira Code', monospace;
            font-size: 90%;
            color: #004D40;
        }
        blockquote {
            border-left: 5px solid #009688;
            background-color: #e0f7fa;
            padding: 12px 20px;
            font-style: italic;
            color: #00695c;
            border-radius: 8px;
            margin: 20px 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 25px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
        }
        th, td {
            border: 1px solid #009688;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #00796B;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #b2dfdb;
        }
    </style>
    """
    return HTML(styles)
