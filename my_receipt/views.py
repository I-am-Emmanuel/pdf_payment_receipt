from django.shortcuts import render
from django.http import FileResponse

from . goods import *
from core.models import UserModel
from . models import PaymentReceipt
from . serializers import PaymentReceiptSerializer

from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

import io

from reportlab.pdfgen import canvas

# Create your views here.


class PaymentReceiptViewSet(generics.GenericAPIView):
    queryset = PaymentReceipt.objects.all()
    serializer_class = PaymentReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            customer = UserModel.objects.filter(email=request.user.email).first()
            receipt = PaymentReceipt(customer=customer, items_purchased=product(), amount=payment(), date=datetime.now())
            receipt.save()
            serializer = self.serializer_class(receipt)
            # return Response(serializer.data, status=201)

        # except Exception as error_message:
        #     return Response({'error': str(error_message)}, status=400)
        
            # Create PDF receipt
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, "Payment Receipt")
            p.drawString(100, 700, "Customer Name: {}".format(serializer.data['customer']['first_name']))
            p.drawString(100, 650, "Items Purchased: {}".format(serializer.data['items_purchased']))
            p.drawString(100, 600, "Amount Paid: {}".format(serializer.data['amount']))
            # p.drawString(100, 600, "Date: {}".format(serializer.data['date']))
            p.showPage()
            p.save()
            buffer.seek(0)
            # Return PDF response
            return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')
        except Exception as error_message:
            return Response({'error': str(error_message)}, status=400)



