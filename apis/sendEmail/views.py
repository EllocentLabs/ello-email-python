from apis.sendEmail.serializers import EmailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from business_logic.sendMail import signup
from business_logic.sendGrid import signUp


class SmtpApi(APIView):
    def post(self, request):
        ser = EmailSerializer(data=request.data)
        if ser.is_valid():
            email = ser.data['email']
            name = 'Ellocent'
            signup(email, name)
            return Response({"status": True, "msg": "Email sent"}, status=200)
        return Response({"status": False, "msg": ser.errors}, status=400)


class SendGridApi(APIView):
    def post(self, request):
        ser = EmailSerializer(data=request.data)
        if ser.is_valid():
            email = ser.data['email']
            name = 'Ellocent'
            signUp(email, name)
            return Response({"status": True, "msg": "Email sent"}, status=200)
        return Response({"status": False, "msg": ser.errors}, status=400)
    pass
