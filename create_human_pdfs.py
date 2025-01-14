import os
from xhtml2pdf import pisa
import pandas as pd
from italian_ats_evaluator import TextAnalyzer

DOCUMENT_REVERSE_MAP = {
    "99bdc9fdd8097f067f77cb220074b1b5": "basilicata",
    "07108e7d68b7e897ed6a800be9802105": "calabria",
    "2f4c39c9fb796e5066ac28770c5724d6": "campania",
    "396505aaf67c46b9ec1a6818d8fb9af6": "lazio",
    "3e0abd25f3bcf417e9e0a8b74e158ef5": "lombardia",
    "6d52bcc84ee3fa9bfec74bb009537bd2": "molise",
    "70da2ae575436d19518deae1ff2125b0": "toscana",
    "aae5c6f0c213946d265cb98c08106c0b": "veneto",
}


def space(n):
    return "&nbsp;" * n


def eval_words(tokenized_documents):
    words = set()
    for document in tokenized_documents:
        for word in document.split():
            word = word.lower()
            words.add(word)
    return len(words)


def parse_stylo_metrics(_o, _r1, _r2, _g):
    html = "<tr>"
    for paragraph, reviewer in zip([_o, _r1, _r2, _g], ['original', 'reviewer1', 'reviewer2', 'gpt4']):
        html += f"""
        <td class="stylo-td">
            Words:{TextAnalyzer(paragraph[f'{reviewer}_text']).basic.n_words}{space(4)}Token:{paragraph[f'{reviewer}_n_tokens']}{space(4)}Chars:{paragraph[f'{reviewer}_n_chars']}<br/>
            Frasi:{paragraph[f'{reviewer}_n_sentences']}{space(6)}Punteggiatura:{paragraph[f'{reviewer}_n_punctuations']}<br/>
            Nomi:{paragraph[f'{reviewer}_n_nouns']}{space(4)}Avverbi:{paragraph[f'{reviewer}_n_adverbs']}{space(4)}Pronomi:{paragraph[f'{reviewer}_n_pronouns']}{space(4)}Articoli:{paragraph[f'{reviewer}_n_articles']}{space(4)}Aggettivi:{paragraph[f'{reviewer}_n_adjectives']}<br/>
            Verbi:{paragraph[f'{reviewer}_n_verbs']}{space(4)}Verbi attivi:{paragraph[f'{reviewer}_n_active_verbs']}{space(4)}Verbi passivi:{paragraph[f'{reviewer}_n_passive_verbs']}
        </td>
        """
    html += "</tr>"
    return html


def parse_readability_metrics(_o, _r1, _r2, _g):
    html = "<tr>"
    for paragraph, reviewer in zip([_o, _r1, _r2, _g], ['original', 'reviewer1', 'reviewer2', 'gpt4']):
        html += f"""
        <td class="readability-td">
            VdB: {round(paragraph[f'{reviewer}_n_vdb'] / paragraph[f'{reviewer}_n_tokens'], 2)} % <br/>
            Gulpease: {round(paragraph[f'{reviewer}_gulpease'], 2)}{space(31)}Flesch Vacca: {round(paragraph[f'{reviewer}_flesch_vacca'], 2)}
        </td>
        """
    html += "</tr>"
    return html


def parse_diff_metrics(_r1, _r2, _g):
    html = "<tr>"
    html += f"<td class=\"diff-td\"></td>"
    for paragraph, reviewer in zip([_r1, _r2, _g], ['reviewer1', 'reviewer2', 'gpt4']):
        html += f"""
        <td class="diff-td">
            similarity:{round(paragraph[f'{reviewer}_semantic_similarity'], 2)}{space(4)}edit_distance:{paragraph[f'{reviewer}_editdistance']}<br/>
            added tokens:{round(paragraph[f'{reviewer}_n_added_tokens'], 2)}{space(4)}added vdb tokens:{round(paragraph[f'{reviewer}_n_added_vdb_tokens'], 2)}<br/>
            deleted_tokens:{paragraph[f'{reviewer}_n_deleted_tokens']}{space(4)}deleted_not_vdb_tokens:{paragraph[f'{reviewer}_n_deleted_vdb_tokens']}<br/>
        </td>
        """
    html += "</tr>"
    return html


def html_template(_original, _reviewer1, _reviewer2, _gpt4):
    html = """
    <html>
    <head>
        <title>PDF</title>
        <style>
            @page {
                size: a4 landscape;
                margin-left: 0.35cm;
                margin-right: 0.35cm;
                margin-top: 0.25cm;
                margin-bottom: 0.25cm;
            }
            .page-content {
                width: 29cm;
                height: 20.5cm;
            }
            h1 {
                width: 29cm;
                height: 0.5cm;
                line-height: 1;
                font-size: 12px;
                text-align: center;
            }
            table {
                width: 29cm;
                height: 20cm;
            }
            td, th {
                margin: 0;
                border: 0;
                padding-top: 0;
                padding-bottom: 0;
                padding-left: 0.15cm;
                padding-right: 0.15cm;
            }
            tr {
                margin: 0;
                border: 0;
                padding: 0;
            }
            .text-th {
                text-align: center;
                width: 7.25cm;
                height: 0.5cm;
                line-height: 1;
                font-size: 11px;
                vertical-align: middle;
            }
            .text-td {
                text-align: justify;
                width: 7.25cm;
                height: 15.7cm;
                line-height: 1.2;
                font-size: 11px;
                vertical-align: top;
            }
            .stylo-td {
                text-align: left;
                width: 7.25cm;
                height: 1.5cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
            .readability-td {
                text-align: left;
                width: 7.25cm;
                height: 1cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
            .diff-td {
                text-align: left;
                width: 7.25cm;
                height: 1cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
        </style>
    </head>
    """

    html += "<body>"

    for _o, _r1, _r2, _g in zip(_original, _reviewer1, _reviewer2, _gpt4):
        _o['original_text'] = _o['original_text'].replace('\n', '<br>')
        _r1['reviewer1_text'] = _r1['reviewer1_text'].replace('\n', '<br>')
        _r2['reviewer2_text'] = _r2['reviewer2_text'].replace('\n', '<br>')
        _g['gpt4_text'] = _g['gpt4_text'].replace('\n', '<br>')
        html += f"""
        <div class="page-content">
            <h1>Paragrafo {_o['paragraph_index']}</h1>
            <table>
                <tr>
                    <th class="text-th">Original</th>
                    <th class="text-th">Reviewer1 ({_r1['reviewer1_time']}s)</th>
                    <th class="text-th">Reviewer2 ({_r2['reviewer2_time']}s)</th>
                    <th class="text-th">GPT-4</th>
                </tr>
                <tr>
                    <td class="text-td">{_o['original_text']}</td>
                    <td class="text-td">{_r1['reviewer1_text']}</td>
                    <td class="text-td">{_r2['reviewer2_text']}</td>
                    <td class="text-td">{_g['gpt4_text']}</td>
                </tr>
                {parse_stylo_metrics(_o, _r1, _r2, _g)}
                {parse_readability_metrics(_o, _r1, _r2, _g)}
                {parse_diff_metrics(_r1, _r2, _g)}
            </table>
        </div>
        """
    html += "</body>"
    html += "</html>"
    return html


if __name__ == "__main__":
    original_df = pd.read_csv('./corpora_with_metrics/original.csv', encoding='utf-8')
    reviewer1_df = pd.read_csv('./corpora_with_metrics/reviewer1.csv', encoding='utf-8')
    reviewer2_df = pd.read_csv('./corpora_with_metrics/reviewer2.csv', encoding='utf-8')
    gpt4_df = pd.read_csv('./corpora_with_metrics/gpt4.csv', encoding='utf-8')

    documents = original_df['document'].unique()
    for document in documents:
        original = original_df[original_df['document'] == document].sort_values(by='paragraph_index').to_dict(orient='records')
        reviewer1 = reviewer1_df[reviewer1_df['document'] == document].sort_values(by='paragraph_index').to_dict(orient='records')
        reviewer2 = reviewer2_df[reviewer2_df['document'] == document].sort_values(by='paragraph_index').to_dict(orient='records')
        gpt4 = gpt4_df[gpt4_df['document'] == document].sort_values(by='paragraph_index').to_dict(orient='records')
        with open(f'./human_pdf/{document}.pdf', 'w+b') as f:
            pisa.CreatePDF(html_template(original, reviewer1, reviewer2, gpt4), dest=f)
