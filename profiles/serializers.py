from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Accesses context obj that views passed into serializer
        '''
        request = self.context['request']
        # Returns True if user is object owner
        # Feeds into variable above, then displayed with Meta class below
        return request.user == obj.owner
    #

    class Meta:
        model = Profile
        fields = [
            # or '__all__' (but 'is_owner' is additional)
            'id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image', 'is_owner'
        ]
