import os

def validate_helm_chart(helm_chart):
    os.system(f'helm lint {helm_chart}')