# .to_representation() - Override this to support serialization, for read operations.
# .to_internal_value() - Override this to support deserialization, for write operations.
# .create() and .update() - Override either or both of these to support saving instances.

from rest_framework import serializers

class HighScoreSerializer(serializers.BaseSerializer):
    
    def to_internal_value(self, instance):
        player_name=instance.get('player_name')
        score=instance.get('score')
        if not player_name:
            raise serializers.ValidationError({
                'player_name':'player_name is required.'
            })
        elif not score:
            raise serializers.ValidationError({
                'score':'Score is required.'
            })
        # elif len(player_name)>20 :
        #     raise serializers.ValidationError({
        #         'player_name':'Playername is less than 20 chracters.'
        #     })
         # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'score': score,
            'player_name': player_name
        }
    
    # def to_representation(self, instance):
    #     return {
    #         'score': instance.score,
    #         'player_name': instance.player_name
    #     }
    
        