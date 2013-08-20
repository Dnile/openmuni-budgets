from rest_framework import serializers
from openbudget.apps.accounts.serializers import AccountMin
from openbudget.apps.sheets import models


class SheetItemCommentBaseSerializer(serializers.ModelSerializer):
    """
    Base SheetItemComment serializer, for creating new SheetItemComment instances.
    """

    class Meta:
        model = models.SheetItemComment
        fields = ['comment', 'user']


class SheetItemCommentReadSerializer(SheetItemCommentBaseSerializer):
    """
    Read SheetItemComment serializer, for listing/retrieving SheetItemComment instances.
    """

    user = AccountMin()

    class Meta(SheetItemCommentBaseSerializer.Meta):
        fields = SheetItemCommentBaseSerializer.Meta.fields +\
                 ['uuid', 'user', 'item', 'created_on', 'last_modified']