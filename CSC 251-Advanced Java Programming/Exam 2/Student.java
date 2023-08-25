public class Student
{
   // instance fields
   private String first;
   private String last;
   private int idNum;
   private HealthAcknowledgementForm form;
   
   // no-arg constructor
   public Student()
   {
      first = "";
      last = "";
      idNum = 0;
      form = new HealthAcknowledgementForm();
   }
   
   // constructor that accepts arguments
   public Student(String first, String last, int idNum, HealthAcknowledgementForm form)
   {
      this.first = first;
      this.last = last;
      this.idNum = idNum;
      this.form = new HealthAcknowledgementForm(form); 
   }
   
   // copy constructor
   public Student(Student obj2)
   {
      first = obj2.first;
      last = obj2.last;
      idNum = obj2.idNum;
      form = new HealthAcknowledgementForm(obj2.getForm());
   }
   
   // mutators
   public void setFirst(String first)
   {
      this.first = first;
   }
   
   public void setLast(String last)
   {
      this.last = last;
   }
   
   public void setIdNum(int idNum)
   {
      this.idNum = idNum;
   }
   
   public void setForm(HealthAcknowledgementForm form)
   {
      this.form = new HealthAcknowledgementForm(form);
   }
   
   // accessors
   public String getFirst()
   {
      return first;
   }
   
   public String getLast()
   {
      return last;
   }
   
   public int getIdNum()
   {
      return idNum;
   }
   
   public HealthAcknowledgementForm getForm()
   {
      return new HealthAcknowledgementForm(form);
   }
   
   // toString()
   public String toString()
   {
      return "\nStudent:\n" + 
             "\t\t Name: " + first + " " + last + 
             "\n\t\t ID Number: " + idNum + "\n" +
             form;
   }
   
}