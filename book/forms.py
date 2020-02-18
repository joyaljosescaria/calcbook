from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TabAdd(forms.Form):
    # date
    date_submitted = forms.DateField(
        widget=DateInput(attrs={
            'class':'form-control',
            'id':'date',
            'placeholder':'Date',
        })
    )
    
    bank = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'bank',
            'id' : 'bank',
            'placeholder' : 'Bank',
            'onFocus':'this.select();' 
        })
    )

    janasevana = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'janasevana',
            'id' : 'janasevana',
            'placeholder' : 'Janasevana',
            'onFocus':'this.select();'
        })
    )
    borrow = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'borrow',
            'id' : 'borrow',
            'placeholder' : 'Borrow',
            'onFocus':'this.select();'
        })
    )
    internet = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'internet',
            'id' : 'internet',
            'placeholder' : 'Internet',
            'onFocus':'this.select();'
        })
    )
    utilities = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'utilities',
            'id' : 'utilities',
            'placeholder' : 'Utilities',
            'onFocus':'this.select();'
        })
    )
    recharge = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'recharge',
            'id' : 'recharge',
            'placeholder' : 'Recharge',
            'onFocus':'this.select();'
        })
    )
    inhand = forms.FloatField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'name' : 'inhand',
            'id' : 'inhand',
            'placeholder' : 'Inhand',
            'onFocus':'this.select();'
        })
    )
    
    

 
