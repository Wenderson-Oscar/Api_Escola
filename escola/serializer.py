from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula, Cliente
from escola.validadores import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validador(self, data):
        if not validar_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"O cpf deve ter 11 dígitos"})

        return data
...
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validar_cpf(self, cpf):
        if(len(cpf) != 11):
            raise serializers.ValidationError("O cpf deve ter 11 dígitos")
        return cpf
    
    def validar_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo")
        return nome 
    
    def validar_rg(self, rg):
        if(len(rg) != 9):
            raise serializers.ValidationError("O rg deve ter 9 dígitos")
        return rg

    def validar_celular(self, celular):
        if(len(celular) < 11):
            raise serializers.ValidationError("O celular deve ter no mínimo 11 dígitos")
        return celular


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome',]
