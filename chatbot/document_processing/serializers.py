from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Document model serializer.
    """

    document = serializers.FileField()

    class Meta:
        model = Document
        fields = ['id', 'document_type', 'content', 'pinecone_index_id']
