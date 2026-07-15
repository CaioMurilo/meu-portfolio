from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField # Importação do novo editor

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    bio = models.TextField(help_text="Resumo para a página inicial.", verbose_name="Biografia")
    profile_picture = models.ImageField(upload_to='profile/', verbose_name="Foto de Perfil")
    
    # Campo para o currículo em PDF
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Faça o upload do seu currículo em PDF", verbose_name="Currículo (PDF)")
    
    github_link = models.URLField(blank=True, null=True, verbose_name="Link do GitHub")
    linkedin_link = models.URLField(blank=True, null=True, verbose_name="Link do LinkedIn")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return self.name

class HomeSection(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Título")
    content = HTMLField(help_text="Texto extra com suporte a imagens, links e negrito.", verbose_name="Conteúdo")
    order = models.IntegerField(default=0, verbose_name="Ordem de Exibição")
    
    class Meta:
        ordering = ['order']
        verbose_name = "Seção da Página Inicial"
        verbose_name_plural = "Seções da Página Inicial"

    def __str__(self):
        return self.title if self.title else f"Seção {self.order}"

class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug (URL)")
    content = HTMLField(help_text="Crie sua página completa aqui.", verbose_name="Conteúdo")
    
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug (URL)")
    description = models.TextField(help_text="Resumo curto para o cartão na página inicial.", verbose_name="Descrição Curta")
    detailed_content = HTMLField(blank=True, null=True, help_text="História completa do projeto para a página de detalhes.", verbose_name="Conteúdo Detalhado")
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True, help_text="Foto principal (Capa)", verbose_name="Imagem de Capa")
    repo_link = models.URLField(blank=True, null=True, verbose_name="Link do Repositório (GitHub)")
    created_at = models.DateField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Galeria de Fotos e Vídeos do Projeto
class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, related_name='gallery', on_delete=models.CASCADE, verbose_name="Projeto")
    file = models.FileField(upload_to='projects/gallery/', verbose_name="Arquivo (Foto ou Vídeo)")
    is_video = models.BooleanField(default=False, help_text="Marque esta caixa se o arquivo for um vídeo (mp4)", verbose_name="É um vídeo?")

    class Meta:
        verbose_name = "Mídia do Projeto"
        verbose_name_plural = "Mídias do Projeto"