from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Screenshot
from .serializers import ScreenshotSerializer

# স্ক্রিনশট আপলোড API
class ScreenshotUploadView(generics.CreateAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser) # ইমেজ আপলোডের জন্য জরুরি

    def perform_create(self, serializer):
        # অটোমেটিকালি বর্তমান ইউজারকে এসাইন করবে সিরিয়ালাইজারের মাধ্যমে
        serializer.save()