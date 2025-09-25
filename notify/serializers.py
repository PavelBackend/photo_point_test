from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    chat_id = serializers.IntegerField(required=False)
    # phone = serializers.CharField(required=False)
    message = serializers.CharField()

    def validate(self, data):
        if not data.get("email") and not data.get("chat_id"):
            raise serializers.ValidationError("Нужен хотя бы один канал уведомлений (email или chat_id).")
        return data
