from datetime import datetime

from rest_framework import generics
from .serializers import LoanSerializer
from .models import Loan


class RegisterLoan(generics.CreateAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        date = datetime.now().date()
        serializer.save(date=date)
