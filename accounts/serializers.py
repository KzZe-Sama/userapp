from rest_framework import fields, serializers
from .models import User, Address, Phone


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        # fields = ['user_id', 'address_location', 'is_default']


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
        # fields = ['user_id', 'phone_number', 'is_default']


class UserView(serializers.ModelSerializer):
    password = serializers.CharField(max_length=75, min_length=10,style={'input_type': 'password'}, write_only=True)
    address = AddressSerializer(many=True)
    phone = PhoneSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['email', 'user_name', 'first_name', 'last_name', 'addresses', 'phones','password']
