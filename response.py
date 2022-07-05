import pytextnow
import time
import os
def sample_response():
  client = pytextnow.Client("u.tlive006",sid_cookie=os.environ['sid'],csrf_cookie=os.environ['csrf'])
  new_messages = client.get_unread_messages()
  #print(new_messages)
  if not new_messages:
    new_messages = client.get_unread_messages()
    return "Not recieved otp yet , try again"
  else:
    for message in new_messages:
      message.mark_as_read()
      messageData = "```" + message.content + "```"
      otpVar = "OTP is " + messageData + " tap to copy"
      return otpVar
  return "error in getting otp try again "