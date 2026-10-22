#!/usr/bin/env python3
"""
Script de CI e Verificação de Integridade da Documentação e Exemplos
Projeto: Formatador de OS (SMAURB)
"""

import os
import sys
import re
import subprocess


def log(msg, status="INFO"):
    colors = {
        "INFO": "\033[94m",
        "PASS": "\033[92m",
        "FAIL": "\033[91m",
        "WARN": "\033[93m"
    }
    reset = "\033[0m"
    print(f"{colors.get(status, '')}[{status}]{reset} {msg}")


def check_markdown_links(docs_dir):
    """
    Varre todos os arquivos markdown e verifica se os links relativos apontam para arquivos existentes.
    """
    log("Iniciando verificação de integridade de links markdown...", "INFO")
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    errors = []
    total_links = 0

    for root, _, files in os.walk(docs_dir):
        for f in files:
            if not f.endswith(".md"):
                continue
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as md_file:
                content = md_file.read()

            for match in link_pattern.finditer(content):
                target = match.group(2).strip()
                # Ignora links externos, links de âncoras locais simples e esquemas file/http
                if target.startswith("http://") or target.startswith("https://") or target.startswith("#") or target.startswith("mailto:"):
                    continue
                if target.startswith("file://"):
                    # Verifica caminho absoluto do file://
                    path_clean = target.replace("file://", "").split("#")[0]
                    # URL unquote
                    import urllib.parse
                    path_clean = urllib.parse.unquote(path_clean)
                    if not os.path.exists(path_clean):
                        errors.append(f"{filepath}: link absoluto inexistente '{target}' -> '{path_clean}'")
                    total_links += 1
                    continue

                # Trata links relativos
                target_clean = target.split("#")[0]
                if not target_clean:
                    continue

                resolved_path = os.path.normpath(os.path.join(root, target_clean))
                total_links += 1
                if not os.path.exists(resolved_path):
                    errors.append(f"{filepath}: link relativo quebrado '{target}' -> '{resolved_path}'")

    if errors:
        for err in errors:
            log(err, "FAIL")
        log(f"Falha na validação de links: {len(errors)} erros encontrados em {total_links} links.", "FAIL")
        return False

    log(f"Todos os {total_links} links validados com sucesso!", "PASS")
    return True


def run_e2e_tests():
    """
    Executa a suíte de testes de regressão E2E via pytest.
    """
    log("Executando suíte de testes E2E e validação dos exemplos...", "INFO")
    test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tests", "test_e2e.py"))
    
    cmd = [sys.executable, "-m", "pytest", test_file, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        log("Falha na execução dos testes E2E!", "FAIL")
        print(result.stdout)
        print(result.stderr)
        return False

    log("Suíte de testes E2E aprovada com sucesso!", "PASS")
    return True


def run_mkdocs_strict():
    """
    Compila a documentação com o MkDocs no modo estrito (--strict).
    """
    log("Executando compilação MkDocs em modo estrito (--strict)...", "INFO")
    root_config = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "mkdocs.yml"))
    docs_config = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mkdocs.yml"))
    config_file = root_config if os.path.exists(root_config) else docs_config

    cmd = ["mkdocs", "build", "-f", config_file, "--strict"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        log("Falha na compilação estrita do MkDocs!", "FAIL")
        print(result.stdout)
        print(result.stderr)
        return False

    log("MkDocs compilado com sucesso sem avisos ou erros!", "PASS")
    return True


def main():
    docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    success = True

    log("=== INÍCIO DO PIPELINE DE INTEGRAÇÃO CONTÍNUA (CI) ===", "INFO")

    if not check_markdown_links(docs_dir):
        success = False

    if not run_e2e_tests():
        success = False

    if not run_mkdocs_strict():
        success = False

    if not success:
        log("=== O PIPELINE DE CI FALHOU! VERIFIQUE OS ERROS ACIMA. ===", "FAIL")
        sys.exit(1)

    log("=== PIPELINE DE CI EXECUTADO COM SUCESSO TOTAL! ===", "PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
