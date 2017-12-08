SqlDataAdapter myCommand = new SqlDataAdapter(
"SELECT au_lname, au_fname FROM authors WHERE au_id = '" + 
 SSN.Text + "'", myConnection);

// Use stored procedures
SqlDataAdapter myCommand = new SqlDataAdapter(
                                "LoginStoredProcedure '" + 
                                 SSN.Text + "'", myConnection);
