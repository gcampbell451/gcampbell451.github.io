public class HealthAcknowledgementForm
{
  // static field to track total number of forms
  private static int totalForms = 0;
  
  // instance fields
  private boolean contactInPastTwoWeeks;
  private boolean isVaccinated;
  private boolean hadSymptomsInPastTwoWeeks;
  
  // no-arg constructor
  public HealthAcknowledgementForm()
  {
     contactInPastTwoWeeks = true;
     isVaccinated = false;
     hadSymptomsInPastTwoWeeks = true; 
     
     // increment total number of forms
     totalForms++;   
  }
  
  // constructor that accepts arguements
  public HealthAcknowledgementForm(boolean contactInPastTwoWeeks, boolean isVaccinated, boolean hadSymptomsInPastTwoWeeks)
  {
     this.contactInPastTwoWeeks = contactInPastTwoWeeks;
     this.isVaccinated = isVaccinated;
     this.hadSymptomsInPastTwoWeeks = hadSymptomsInPastTwoWeeks; 
     
     // increment total number of forms
     totalForms++;    
  }
  
  // copy constructor
  public HealthAcknowledgementForm(HealthAcknowledgementForm obj2)
  {
     contactInPastTwoWeeks = obj2.contactInPastTwoWeeks;
     isVaccinated = obj2.isVaccinated;
     hadSymptomsInPastTwoWeeks = obj2.hadSymptomsInPastTwoWeeks;
  }
  
  // mutators
  public void setContactInPastTwoWeeks(boolean contactInPastTwoWeeks)
  {
     this.contactInPastTwoWeeks = contactInPastTwoWeeks;
  }
  
  public void setIsVaccinated(boolean isVaccinated)
  {
     this.isVaccinated = isVaccinated;
  }
  
  public void setHadSymptomsInPastTwoWeeks(boolean hadSymptomsInPastTwoWeeks)
  {
     this.hadSymptomsInPastTwoWeeks = hadSymptomsInPastTwoWeeks;
  }
  
  // accessors
  public boolean getContactInPastTwoWeeks()
  {
     return contactInPastTwoWeeks;
  }
  
  public boolean getIsVaccinated()
  {
     return isVaccinated;
  }
  
  public boolean getHadSymptomsInPastTwoWeeks()
  {
     return hadSymptomsInPastTwoWeeks;
  }
  
  public static int getTotalForms()
  {
     return totalForms;
  }
  
  // method to determine if student can return and if conditions apply to their return
  public String returnConditions(boolean contactInPastTwoWeeks, boolean isVaccinated, boolean hadSymptomsInPastTwoWeeks)
  {
     if (isVaccinated && !hadSymptomsInPastTwoWeeks)
        return "Student is allowed to return to campus with no restrictions";
     else if ((isVaccinated && contactInPastTwoWeeks) || !isVaccinated)
        return "Student is allowed to return to campus but must wear a mask";
     else 
        return "Student is not allowed to return to campus";
  }
  
  // toString method
  public String toString()
  {
     
     return "Health Acknowledgement Form:\n" + 
            "\t\t In Contact with COVID-19: " + contactInPastTwoWeeks + 
            "\n\t\t Vaccinated: " + isVaccinated + 
            "\n\t\t Displaying COVID-19 Symptoms: " + hadSymptomsInPastTwoWeeks + "\n" + 
            returnConditions(contactInPastTwoWeeks, isVaccinated, hadSymptomsInPastTwoWeeks) + "\n";
  }
  
}