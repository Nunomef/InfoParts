from oscar.apps.dashboard.partners.forms import PartnerCreateForm as CorePartnerCreateForm

class PartnerCreateForm(CorePartnerCreateForm):
    
    class Meta(CorePartnerCreateForm.Meta):
        
        fields = ['name', 'email', 'phone_number', 'mobile_number']