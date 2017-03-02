
# coding: utf-8

# In[1]:

import re

notes_header = ['Source Path', 'UniqueId14M', 'LoanTypeIdDesc', 'PaymentType', 'OrigMtgDt', 'OrigProductionsFundDt',                'USPSFullAddr', 'USPSCity' , 'USPSState', 'USPSZip5', 'OrigLoanAmt', 'LenderName',                 'OrigNoteRate', 'OrigARMNoteRate14M', 'OrigFirstPmtDueDt', 'OrigIntOnlyFlag',                'OrigIntOnlyExpDt', 'OrigMaturityDt', 'ARMInitialRateResetMon', 'OrigAmortTermMonths',                'OrigIntOnlyTermMon',  'OrigLoanTypeId', 'OrigPIAmt', 'Change Date', 'ARMRecastFreqMonths',                'OrigARMIndexCd14M', 'ARMMarginRate14M', 'ARMSubseqAdjCapRate', 'ARMFloorRate',                 'OrigARMLifeCapRate', 'OrigARMFloorRate14M', 'OrigARMCeilingRate14M','PayoffPenaltyFlag',                 'PayoffPenaltyWinMonths', 'OrigChannelNum', 'Paragraphs Not Found' ,'Document Type']

source_path_index = 0
loan_number_index = 1
loan_type_index = 2
payment_type_index = 3
mortgage_date_index = 4
productions_fund_date_index = 5
usps_full_address_index= 6
usps_city_index = 7
usps_state_index = 8
usps_zip_index = 9
loan_amount_index = 10
lender_name_index = 11
note_rate_index = 12
arm_initial_rate_index = 13
first_payment_date_index = 14
interest_only_at_origination_flag_index = 15
interest_only_exp_date_index = 16
maturity_date_index = 17
initial_rate_period_index = 18
loan_term_index = 19
interest_only_term_index = 20
interest_type_at_origination_index = 21
pi_amount_index = 22
change_date_index = 23
arm_payment_reset_freq_index= 24
arm_index_index = 25
arm_margin_at_origination_index = 26
arm_periodic_rate_cap_index = 27
arm_periodic_rate_floor_index = 28
arm_lifetime_rate_cap_index = 29
arm_lifetime_rate_floor_index = 30
arm_lifetime_rate_ceiling_index = 31
prepayment_penalty_flag_index = 32
prepayment_penalty_term_index = 33
loan_source_index = 34
paragraphs_not_found_index = 35

# Regex for markers
note_re_string = '[NM]\s{0,}[OQo0]{0,1}.{0,1}[TLI].{0,1}[EC]'
note_re = re.compile(note_re_string)

fixed_re_string = '(?i)F\s{0,}[il]\s{0,}.{0,1}[xnvcl]\s{0,}[ecil]{0,1}\s{0,}[dj]{0,1}'
adjustable_re_string = '[AQ][DB][JIL\s]\s{0,1}[UIOL\s]\s{0,}S[TI]A[BEH][LI]E\s{0,}.{3,5}\s{0,}'
equity_re_string = 'EQUITY\s{0,}'
promissory_re_string = '.[RN][OQ][MN]\s{0,}[IlLHJ\]R].{0,2}[S]\s{0,}[S][OQGg\s]\s{0,}[R\sN].{0,2}\s{0,}'
balloon_re_string = 'BALLOON\s{0,}'
consolidated_re_string = 'CON\s{0,}SOLIDATE{0,1}.\s{0,}'
restated_re_string = 'RESTATED\s{0,}'
interest_only_period_re_string = 'INTEREST.{0,1}ONLY\s{0,}PERIOD\s{0,}'
addendum_re_string = 'ADDENDUM\s{0,}'
allonge_re_string = 'ALL[O0]NGE\s{0,}'
multistate_re_string = '.{0,4}[TI]S[TIY]A[TI]E\s{0,}'

adjustable_re = re.compile(adjustable_re_string)
fixed_re= re.compile(fixed_re_string)
equity_re = re.compile(equity_re_string)
promissory_re = re.compile(promissory_re_string)
balloon_re = re.compile(balloon_re_string)
restated_re = re.compile(restated_re_string)
interest_only_period_re = re.compile(interest_only_period_re_string)
addendum_re = re.compile(addendum_re_string)
allonge_re = re.compile(allonge_re_string)
multistate_re = re.compile(multistate_re_string)

#consolidated_adjustable_re = re.compile(consolidated_re_string + adjustable_re_string + note_re_string) 
# We don't want this (just saw one where this is good)

loan_type_re_string = '(' + adjustable_re_string + '|' + equity_re_string + '|' + promissory_re_string + '|' + balloon_re_string + '|' + restated_re_string + '|' + consolidated_re_string + ')' + note_re_string
loan_type_re = re.compile(loan_type_re_string)

date_re = re.compile('[\[\{\(l\|]D\s{0,1}[ai].{0,1}[tlKrv]{1,2}[eoca][\]\}\)\sl\|]')
city_re = re.compile('[\[\{\(\|lY]\s{0,1}C.{0,2}[trR][yvY][\]\}\)\|l]')
state_re = re.compile('[\[\{\(\|l]\s{0,1}S[tl]a[tl][eco][\]\}\)\|lt]')

# Regex's for dates
letters_could_be_numbers = 'OoDUuLlIi!\|\[\]\(\)\{\}ZzSsGB'
# We always have full month names for the Notes
# months_re_string = '(?i)((Jan(?:uary)?)|(Feb(?:ruar[yv])?)|(Mar(?:ch)?)|(Apr(?:il)?)|(May)|([JL]un(?:e)?)|\
# (Jul(?:y)?)|(Aug(?:u[sa]t)?)|(Sep(?:tember)?)|(Oct(?:ober)?)|(Nov(?:ember)?)|(Dec(?:ember)?))'
months_re_string = '(?i)(([JI\)]an[ua]{1,3}[rm]y)|([FE][ec]bruar[yv])|(March)|(A\s{0,}p\s{0,}r\s{0,}[ilt1\s]{2,3})|(May)|([JLT\)]\s{0,}[ui0]\s{0,}[nm]\s{0,}e)|([JI\)]u\s{0,}[lt1I]y)|(Aug[ug][sa]t)|(Sep[tb]em\s{0,1}ber)|(O{0,1}ctober)|(Nov[em]{2}ber)|([Dp]ec[em][mne]{1,2}[be]{2}r{0,1}))'
date_number_re_string = '[\d' + letters_could_be_numbers + ']'
# The day could have 1 or 2 digits
complete_date_re_string = '(' + months_re_string + '\s{0,}[,\.]{0,1}\s{0,}' + '(.{0,3}\s{0,}' + date_number_re_string + '{0,1}\s{0,}' + date_number_re_string + '{0,1}\s{0,}' + '.{0,3}\s{0,}'  +  ')'+ '[,\.\s]\s{0,}' + '(' + date_number_re_string + '\s{0,}' + date_number_re_string + '\s{0,}' + date_number_re_string + '\s{0,}' + date_number_re_string + ')' + ')'
# Note - the .{0,3} is just for the unreadable characters that sometimes replace the ordinal stuff
# or sometimes a random character is inserted before or after the number



complete_date_re = re.compile(complete_date_re_string)

clean_months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER',                'NOVEMBER', 'DECEMBER']


property_address_re = re.compile('.{1,6}[riomu]{1,2}p.{1,3}[yzv]\s{0,}[Aa].{0,1}[dl]d{0,1}.[eun]{0,1}[sea]{1,2}[:\]\)\}\|l]|                                 \[Property\]|P[ROM]{1,2}PE[RI][TL]Y\s{0,}ADDRES\s{0,1}S')

# If no colon, the address is above
# I with colon, the address is next to the marker and line below (if it is not empty)

# Check for the zip and state - insert comma before state if not found - to be able to separate the city
state_abbr_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',                   'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',                    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',                   'VA', 'WA', 'WV', 'WI', 'WY', 'DC']

state_names_list_re = re.compile('(ALABAMA)|(ARKANSAS)|(ARIZONA)|(ARKANSAS)|(CALIFORNIA)|(COLORADO)|(CONN.{0,7})'                                  '|(DELAWARE)|(FLOR[IL]DA.{0,1})|(GEORGIA)|(HAWAII)|(IDAHO)|([IL]{4}NOIS)|(INDIANA)|(IOWA)'                                 '|(KANSAS)|(KENTUCKY)|(LOUISIANA)|(MAINE)|(MARYLAND)|(MASSACHUSET{1,2}S)|(MICHIGAN)'                                 '|(MINNESOTA)|(MISSISSIPPI)|(MISSOURI)|(MONTANA)|(NEBRASKA)|(NEVADA)|(NEW HAMPSHIRE)'                                 '|(NEW JERSEY)|(NEW MEX[IL]CO)|(NEW\s{0,}YORK)|(NORTH CAROLINA)|(NORTH DAKOTA)|(OHIO)'                                 '|(OKLAHOMA)|(OREGON)|(PENNSY[LI]VAN[IL]A)|(RHODE ISLAND)|(SOUTH CAROLINA)|(SOUTH DAKOTA)'                                 '|(TENNESSEE)|(TEXAS)|(UTAH)|(VERMONT)|(VIRGINIA)|(WASHINGTON)|(WEST VIRGINIA)'                                 '|(WISCONSIN)|(WYOMING)|(DISTRICT OF COLUMBIA)')


# BORROWER'S PROMISE TO PAY/RIGHT TO PREPAY components
borrowers_re_string = '(?i)[BIE83aD]{1,2}[O0DU][rnaBE]{2}\s{0,1}[O0DU].{0,2}[WV].{0,1}[EOA]{0,1}[RLFN].{0,3}\s{0,}[^A-Z]{0,2}'
promise_re_string = '(?i).{1,2}[RB]{0,1}[OE]{0,1}[MNH][ILT].{0,1}S{0,1}E\s{0,}'
to_pay_re_string = '(?i).{1,5}\s{0,1}[Oo0][E\s]{0,}[PAmFL]{1,2}.{0,1}[YxIlV]'
right_re_string = '(?i)R[Il1E][GC]H.{0,1}[TIl1].{0,1}\s{0,}'
to_prepay_re_string = '(?i).{1,3}[Oo0] [PF][RB]E[PF]AY'

borrowers_promise_to_pay_re_string = borrowers_re_string + promise_re_string +  to_pay_re_string + '|' + 'In return for a loan' + '|' + 'For value received'

interest_uc_re_string = '[Iil1!\]\[\|].{0,1}N.{0,1}T.{0,1}[EF].{0,1}R[EB][SsI].{0,1}[T1I]{0,1}'
interest_lc_re_string = '\d\s{0,}[\.,]{0,1}\s{0,}[Il1i!\]\[\|]nterest|Interest will [bh]e charged'

payment_re_string = '.AY[MIWNVL\s]{1,3}[EIu]{1,2}N.'

payments_re_string = payment_re_string + 'S|\d\s{0,}[,\.]\s{0,}Payments'

time_and_place_of_payments_re_string = '[T\s][ilt][mn][ebc].{0,2}[aj]nd.{0,2}P[lI][a\s][ct]{1,2}[ec]' + '.{2,9}[aon][yv\s]t{0,1}[mn][ec][nua].{1,3}'

interest_rate_and_payment_changes_re_string = '.*' + interest_uc_re_string + '\s{0,}RATE AND.*' + payment_re_string +'.{1,9}AN\s{0,}G\s{0,}ES' + '|' +'Interest Rate and Payment Changes'
change_dates_re_string = 'Change Dates'

borrowers_right_to_prepay_re_string =  borrowers_re_string + right_re_string + to_prepay_re_string + '|' + 'I\s{0,}have the right to make payments'

loan_charges_re_string = 'LOAN CHARGES|Loan Charges'

borrowers_promise_to_pay_re = re.compile(borrowers_promise_to_pay_re_string)
interest_uc_re = re.compile(interest_uc_re_string)
interest_lc_re = re.compile(interest_lc_re_string)
payments_re = re.compile(payments_re_string)
time_and_place_of_payments_re = re.compile(time_and_place_of_payments_re_string)
interest_rate_and_payment_changes_re = re.compile(interest_rate_and_payment_changes_re_string)
change_dates_re = re.compile(change_dates_re_string)
borrowers_right_to_prepay_re = re.compile(borrowers_right_to_prepay_re_string)
loan_charges_re = re.compile(loan_charges_re_string)


thereafter_re_string = '[Tt][hlr]{1,2}[ec]r[ec]a.{2}[ec]r'
    


# In[2]:

import re


def getLoanAndPaymentTypes(line, previous_line, attributes_row, in_file):
# There are cases where the actual NOTE is at the bottom/middle of the document
# Need to check the previous lines since sometimes 'INTEREST ONLY PERIOD' and 'ADJUSTABLE RATE NOTE'
# are in separate lines
    loan_type = cleanLoanType(line)
    attributes_row[loan_type_index] = loan_type
    attributes_row = getPaymentType(loan_type, attributes_row, in_file)
        
    # Check if 'INTEREST-ONLY PERIOD' is in the previous line
    if len(interest_only_period_re.findall(previous_line)) > 0:
        attributes_row[loan_type_index] = 'INTEREST-ONLY PERIOD ' +  attributes_row[loan_type_index]
            
    if debug:
        print('Found loan type: ' + attributes_row[loan_type_index])
        print('Found payment type: ' + attributes_row[payment_type_index] )

    return attributes_row

def cleanLoanType(loan_type):
    
    # If the first word is Note, then the type is just NOTE
    if debug:
        print('Loan type: ' + loan_type)
    
    # Set to all caps
    loan_type = loan_type.upper()
    
    
    # Clean the common words
    if len(adjustable_re.findall(loan_type)) > 0:
        # Convert the regex version to just say 'ADJUSTABLE RATE'
        arn_marker = adjustable_re.findall(loan_type)[0]
        loan_type = loan_type.replace(arn_marker, 'ADJUSTABLE RATE ')
        
    if len(promissory_re.findall(loan_type)) > 0:
        promissory_marker = promissory_re.findall(loan_type)[0]
        loan_type = loan_type.replace(promissory_marker, 'PROMISSORY ')
    
    if len(fixed_re.findall(loan_type)) > 0:
        fixed_marker = fixed_re.findall(loan_type)[0]
        loan_type = loan_type.replace(fixed_marker, 'FIXED ')
    
    
    if len(multistate_re.findall(loan_type)) > 0:
        multistate_marker = multistate_re.findall(loan_type)[0]
        loan_type = loan_type.replace(multistate_marker, 'MULSTISTATE ')
    
    
    
    # Remove everything that is not a letter or space
    # Convert multiple spaces to just one space
    loan_type = re.sub('[^A-Za-z\s/]', '', loan_type).strip()
    loan_type = re.sub('\s+', ' ', loan_type)
        
    # Remove everything after note    
    loan_type_words = loan_type.split()
    loan_type = ''
    for loan_type_word in loan_type_words:
        note_marker = note_re.findall(loan_type_word)
        if len(note_marker) > 0 and loan_type_word == note_marker[0]:
            loan_type = loan_type + ' NOTE'
            break;
        else:
            loan_type = loan_type + ' ' + loan_type_word
    
    # Remove everything before 'FIXED
    fixed_index = loan_type.find('FIXED')
    if fixed_index != -1:
        loan_type = loan_type[fixed_index:]
    
    loan_type = loan_type.strip()
    
    # Split the words by space and if it has less than 3 characters, remove it
    # Remove the extra characters in the beginning
    loan_type_words = loan_type.split()
    if len(loan_type_words[0].strip()) < 3:
        loan_type = ' '.join(loan_type_words[1:])
            
    
    if debug:
        print('Cleaned loan type: ' + loan_type)
              
    return loan_type

def getPaymentType(loan_type, attributes_row, in_file):
    # Get the line below for certail loan types
    payment_type= ''
    if len(adjustable_re.findall(loan_type)) > 0 or len(equity_re.findall(loan_type)) > 0 or    len(balloon_re.findall(loan_type)) > 0 or len(promissory_re.findall(loan_type)) > 0:
        payment_type_found = False
        end_of_file_found = False
        while not (payment_type_found or end_of_file_found):
            payment_type = in_file.readline()
            if len(payment_type) == 0:
                # End of file
                end_of_file_found = True
            else:
                payment_type = payment_type.replace('\n', '').strip()
                if len(payment_type) > 5:
                    this_note_marker_re = re.compile('(?i)TH[EIS]{1,2} NOTE')
                    if len(this_note_marker_re.findall(payment_type)) > 0:
                        # 'THIS NOTE' is not the string we want for payment type
                        payment_type = ''
                        payment_type_found = True
                    elif len(promissory_re.findall(payment_type)) > 0 or                     len(interest_only_period_re.findall(payment_type)) > 0:
                        # There are cases where a promissory note has CONSOLIDATED, RESTATED, etc and the next line
                        # has the words PROMISSORY NOTE. We want the line after this
                        payment_type_found = False
                    else:
                        payment_type_found = True
    
    
    attributes_row[payment_type_index] = cleanPaymentType(payment_type)

    return attributes_row

def cleanPaymentType(payment_type):
    
    # Clean payment type
    start_marker_re = re.compile('[\(\[\{\|C]')
    end_marker_re = re.compile('[\)\]]')

    start_marker = start_marker_re.findall(payment_type)
    end_marker = end_marker_re.findall(payment_type)

    if len(start_marker) > 0 and len(end_marker) > 0:
        start_index = payment_type.find(start_marker[0]) # Get the first one
        end_index = payment_type.find(end_marker[-1]) # Get the last one
        payment_type = payment_type[start_index + 1: end_index]
    elif len(start_marker) > 0:
        start_index = payment_type.find(start_marker[0]) # Get the first one
        payment_type = payment_type[start_index + 1]
    elif len(end_marker) > 0:
        end_index = payment_type.find(end_marker[-1]) # Get the last one
        payment_type = payment_type[:end_index]
        
    treasury_re = re.compile('(?i).{2,3}[ane][sm]u\s{0,}ry')
    index_re = re.compile('(?i)Inde[xk]')
    month_re = re.compile('(?i)mont[hl]{1,2}')
    arm_re = re.compile('AR[MNI\s]{1,2}')
    rate_re = re.compile('R[aui]\s{0,}[tli].{0,1}[eE]')
    cr_re = re.compile('Cons.*v[ec]r')
    
    if len(treasury_re.findall(payment_type)) > 0:
        # Convert the regex version to just say 'Treasury'
        treasury_marker = treasury_re.findall(payment_type)[0]
        payment_type = payment_type.replace(treasury_marker, 'Treasury ')
        if debug:
            print('Treasury marker + cleaned payment type: ', str(treasury_marker), payment_type)

    if len(index_re.findall(payment_type)) > 0:
        # Convert the regex version to just say 'Index'
        index_marker = index_re.findall(payment_type)[0]
        payment_type = payment_type.replace(index_marker, 'Index ')
        if debug:
            print('Index marker + cleaned payment type: ', str(index_marker), payment_type)

    if len(month_re.findall(payment_type)) > 0:
        # Convert the regex version to just say 'Month'
        month_marker = month_re.findall(payment_type)[0]
        payment_type = payment_type.replace(month_marker, 'Month ')
        if debug:
            print('Month marker + cleaned payment type: ', str(month_marker), payment_type)
        
    if len(arm_re.findall(payment_type)) > 0:
        # Convert the regex version to just say 'Index'
        arm_marker = arm_re.findall(payment_type)[0]
        payment_type = payment_type.replace(arm_marker, 'ARM ')
        if debug:
            print('ARM marker + cleaned payment type: ', str(arm_marker), payment_type)
        
    if len(fixed_re.findall(payment_type)) > 0:
        fixed_marker = fixed_re.findall(payment_type)[0]
        payment_type = payment_type.replace(fixed_marker, 'Fixed ')
        if debug:
            print('Fixed marker + cleaned payment type: ', str(fixed_marker), payment_type)
    
    if len(rate_re.findall(payment_type)) > 0:
        rate_marker = rate_re.findall(payment_type)[0]
        payment_type = payment_type.replace(rate_marker, 'Rate ')
        if debug:
            print('Rate marker + cleaned payment type: ', str(rate_marker), payment_type)

    if len(cr_re.findall(payment_type)) > 0:
        cr_marker = cr_re.findall(payment_type)[0]
        payment_type = payment_type.replace(cr_marker, 'Construction/Rollover')
        if debug:
            print('Construction/Rollover marker + cleaned payment type: ', str(cr_marker), payment_type)

        
    fixed_rate_re = re.compile('.{0,3}[ecn]d\s{0,}.{0,3}\s{0,}Rate|Fixed\s{0,}[Rmtun]{1,3}')
    if len(fixed_rate_re.findall(payment_type)) > 0: 
        fixed_rate_marker = fixed_rate_re.findall(payment_type)[0]
        payment_type = 'Fixed Rate'
        if debug:
            print('Fixed Rate marker + cleaned payment type: ', str(fixed_rate_marker), payment_type)
        
        
    # Remove everything that is not a letter, number, / or space
    # Convert multiple spaces to just one space
    payment_type = re.sub('[^A-Za-z0-9/\s]', '', payment_type).strip()
    payment_type = re.sub('\s+', ' ', payment_type)
    
    payment_type = payment_type.strip()
    if len(payment_type) < 5:
        payment_type = ''
    return payment_type



def getDateAndCity(line, previous_lines, attributes_row):
    # There are other parts of the document that has one of the 3 and that is not what we want
    
    # Prioritize the lines in previous_lines when getting dates
    # We are just checking the lengths of the lines
    if len(previous_lines[2].strip()) > 10:
        date_line = previous_lines[2]
    elif len(previous_lines[1].strip()) > 10:
        date_line = previous_lines[1]
    else:
        date_line = previous_lines[0]
    
    date_line_splits = re.split(r'\s{5,}', date_line)
    
    # Make sure the date_line_splits only contain "valid" data; Remove a split that do not have alphanumeric characters
    date_line_splits = [date_line_split for date_line_split in date_line_splits                         if (sum(c.isdigit() for c in date_line_split) > 2 or                            sum(c.isalpha() for c in date_line_split) > 2  ) ]

    if debug:
        print('Found date city marker: ' + line)
        print('Date line splits: ' , date_line_splits)

    mortgage_date = ''
    date_city = ''
    split_index = 0
    for split in date_line_splits:
        if len(complete_date_re.findall(split)) > 0:
            # This split has the date
            mortgage_date = split
            break;
        split_index +=1 
    
    if split_index < len(date_line_splits) - 1:
        date_city = date_line_splits[split_index + 1]
    
    if debug: 
        print('Found date: ' + mortgage_date)
        print('Found city: ' + date_city)
    
    if mortgage_date.startswith('Error'):
        cleaned_date = mortgage_date
        formatted_date = ''
    else:
        cleaned_date, formatted_date = cleanAndFormatDate(mortgage_date)
        
    attributes_row[mortgage_date_index] = cleaned_date
    attributes_row[productions_fund_date_index] = cleaned_date
    attributes_row[usps_city_index] = date_city
    
    return attributes_row

def getMortgageDate(line):
    # Get date from line
    # We keep dates until we find 'BORROWERS PROMISE TO PAY'

    line_splits = re.split(r'\s{3,}', line)
    split_with_possible_date = ''
        
    for line_split in line_splits:
        # Check the number of characters (without spaces in each split)
        chars_count = len(line_split.strip().replace(' ', ''))
        if chars_count > 5 and chars_count < 20:
            split_with_possible_date = line_split
            date_marker = complete_date_re.findall(split_with_possible_date)
            if len(date_marker) > 0:
                date = date_marker[0][0]
                remaining_characters = split_with_possible_date.replace(date, '').strip()
                if debug:
                    print('Found the date in: ', split_with_possible_date)
                    print('Date is: ', date)
                return date
            
        
    return ''


def cleanAndFormatDate(date):
    
    if len(date.strip()) == 0:
        return '', ''
    
    if debug:
        print('Input date: ', date)
        
    # Remove . if it is the first/last character in the number
    if date[-1] == '.':
        date = date[:-1]
    if date[0] == '.':
        date = date[1:]
    if debug:
        print('Date after removing . in front/end:', date)
    
    
    # Remove , if it is the first/last character in the number
    if date[-1] == ',':
        date = date[:-1]
    if date[0] == ',':
        date = date[1:]
    if debug:
        print('Date after removing , in front/end:', date)
    
    
    # Remove 'st', 'nd', 'rd', and 'th'
    ordinal_re_string = '[1liIL:\|\[\]\(\)]st|[2Zz]nd|3rd|[45Ss6G78B90OoDUu]th'
    ordinal_re = re.compile(ordinal_re_string)
    ordinal_marker = ordinal_re.findall(date)
    if len(ordinal_marker) > 0:
        ordinal_marker_removed = re.sub('st|nd|rd|th', '', ordinal_marker[0])
        date = date.replace(ordinal_marker[0], ordinal_marker_removed)
    
    if debug:
        print('After removing the ordinal stuff: ', date)
    date_marker = complete_date_re.findall(date)
    cleaned_date = 'Error: Date not found: ' + date
    formatted_date = ''        
    
    if len(date_marker) > 0:
        if debug:
            print('Date marker: ', str(date_marker))
            
        date = date_marker[0][2:]
        # 2: since the first two are the complete date and the month name
        month_found = False
        month_index = 0
        while not month_found and month_index < 12:
            if len(date[month_index].strip()) > 0:
                month_found = True
                break;
            month_index += 1

        month_name = clean_months[month_index]
        month_number = str(month_index+1)
        if len(month_number) == 1:
            month_number = '0' + month_number

        day = date[-2]
        day = day.replace(' ', '')
        if len(day) > 2:
            day = day[0:2]
        day = convertLettersToNumbers(day)
        day = re.sub('[^0-9]', '', day)
        
        
        if len(day) == 0:
            day = '01'
        
        if int(day) > 31:
            day = day[0]
        
        if len(day) == 1:
            day = '0' + day

        year = date[-1]
        year = year.replace(' ', '')
        year = convertLettersToNumbers(year)
        
        # For now, the cleaned date is in the format Month Day, Year (Day is 1 or 2 characters)
        cleaned_date = month_name + ' ' +  str(int(day)) + ', ' + year 
        formatted_date = year + month_number + day

        # Have restrictions/error-checking for date
        if year[0] == '0' or int(year[0]) > 2:
            # This is a wrong year
            cleaned_date = 'Error: Year is wrong: ' + year

        elif year[0] == '1' and year[1] == '0':
            year = '2' + year[1:]
            cleaned_date = month_name + ' ' +  str(int(day)) + ', ' + year 
            formatted_date = year + month_number + day
            
        elif year[0] == '2' and year[1] == '9':
            year = '1' + year[1:]
            cleaned_date = month_name + ' ' +  str(int(day)) + ', ' + year 
            formatted_date = year + month_number + day
            
            
        if debug:
            print(date_marker)
            print(date)
            print(month_name)
            print(month_number)
            print(day)
            print(year)
            print(cleaned_date)

    return cleaned_date, formatted_date

    
def getPropertyAddressFromLines(previous_lines, line_with_date):
    property_address = ''
    # Start from the last line (so switch up the first and last lines)
    temp_line = previous_lines[0]
    previous_lines[0] = previous_lines[2]
    previous_lines[2] = temp_line
    
    for previous_line in previous_lines:
        if len(previous_line.strip()) > 0:    
            if len(property_address.strip()) > 0 and previous_line[-1] != ',':
                # Concatenate lines (remember the lines are reversed in order)
                property_address = ', ' + property_address
            property_address = previous_line + property_address

            if previous_line[0].isdigit():
                # This line starts with a number (which means it is most likely an address), this is the only address line
                break;

    address_words = re.split('\s',property_address) 
    if len(address_words) <= 5:
        if debug:
            print('Address is too short - get the other part from line_with_date')
        line_with_date_splits = re.split('\s{3,}', line_with_date)
        if len(line_with_date_splits) > 1:
            other_address = line_with_date_splits[1].strip()
            property_address =  other_address + ', ' +  property_address 
            
    
    # Get last 6 characters of property_address - remove spaces and convert numbers to letters
    last_6 = property_address[-6:].strip()
    last_6 = re.sub('[\s\.]', '', last_6)
    new_last_6 = convertLettersToNumbers(last_6)
    if new_last_6.isdigit():
        # Don't replace unless we are able to turn it into a zip
        property_address = property_address[:-6] + ' ' + new_last_6
    if debug:
        print('last 6 charcters: ', last_6)
        print('new last 6 characters: ', new_last_6)
        print('new property address: ', property_address)
    
        
    # Find any 5-digit number - get the last occurrence and remove everything else after that (assuming it's the zip)
    zip_re = re.compile('\d{5}')
    zip_re_marker = zip_re.findall(property_address)
    if len(zip_re_marker) > 0:
        zip = zip_re_marker[-1]
        zip_end_index = property_address.find(zip) + 5
        property_address = property_address[:zip_end_index]
        
    if debug:
        print('Previous lines: ', str(previous_lines))
        print('Line with date: ', line_with_date)
        print('Zip marker: ', zip_re_marker)
        print('Property address: ', property_address)
    
    # Change X.Y. to XY
    dot_marker_re = re.compile('[A-Za-z]\.[A-Za-z]\.')
    dot_marker = dot_marker_re.findall(property_address)
    for marker in dot_marker:
        property_address = property_address.replace(marker, marker.replace('.', ''))
    
    if debug:
        print('Property Address after changing X.Y. to XY: ', property_address)
        
    # Replace '.' with ',' in address
    property_address = property_address.replace('.', ',')
    # Replace 2 commas together (since we have replaced . with ,)
    property_address = re.sub(',\s{0,},', ',', property_address)
    
    if debug:
        print('Property Address after replacing the . to , and replacing 2 commas to 1: ', property_address)
    
    if len(property_address.strip()) > 105:
        # This is when the last 3 sentences of a paragraph are mistaken to be the addresses
        if debug:
            print('Property address is too long: ', str(len(property_address.strip())))
        property_address = ''
    return property_address

def streetWordInAddress(street_word, address):
    # Only keep alpha-numeric characters in the address
    address_words = address.split()
    if any (street_word == address_word for address_word in address_words):
        return True
    else:
        return False
    
def getAddressValues(property_address, attributes_row):
           
    if debug: 
        print('Property Address: ' + property_address)
    
    city = attributes_row[usps_city_index]
    
    # Remove anything at the end/beginning that has more than 5 spaces
    address_line_splits = re.split(r'\s{5,}', property_address)
    property_address = ''
    for split in address_line_splits:
        if len(split) > 3:
            property_address = property_address + ' ' + split
    
    # Change address to upper case and replace multiple spaces with just one
    property_address = property_address.strip().upper()
    property_address = re.sub('\s{2,}', ' ', property_address)
    city = city.upper()
    
    if debug:
        print('Property Address after removing the extra stuff at the end/beginning: ', property_address)

    if len(property_address.strip()) == 0:
        return attributes_row

    # Remove 'PROPERTY ADDRESS' from the line (sometimes the marker is not caught if : is not present)
    property_address_marker = property_address_re.findall(property_address)
    if len(property_address_marker) > 0:
        property_address = property_address.replace(property_address_marker[0], '').strip()
    if debug:
        print('Property address marker: ', str(property_address_marker))
    
    
    # Replace a comma surrounded by spaces with just the comma
    property_address = re.sub('\s{0,},\s{0,}', ', ', property_address)
    
    # Replace D.C. with DC
    property_address = re.sub('D\s{0,}[\.,]\s{0,}C\s{0,}[\.,]', 'DC', property_address)
    
    
    # If the address ends or begins with , or ., remove those
    # This makes sure we don't have an empty split
    property_address = property_address.strip()
    if property_address[-1] == '.' or property_address[-1] == ',':
        property_address = property_address[:-1]
    if property_address[0] == '.' or property_address[0] == ',':
        property_address = property_address[0:]
    property_address = property_address.strip()
    
    # Split by space 
    # Do not want to split by comma since we want to keep it in cases where there are multipel street addresses
    address_words = re.split('\s',property_address) 
    if debug:
        print('Address splits by space: ', str(address_words))
        
    # Address are in the form street, city, state, zip
    # However, there are cases when the zip or street are not available
    
    property_street_address = ''
    property_city_address = ''
    property_state_address = ''
    property_zip_address = ''

    property_street_city_address = ''
    property_street_city_state_address = ''
    property_state_zip_address = ''
        
        
    if len(city.strip()) > 0 and city in property_address:
        # City data is in property_address, so can figure out state-zip and street
        address_splits = property_address.split(city)
        property_street_address = address_splits[0].strip()
        property_city_address = city.strip()
        
        property_state_zip_address = address_splits[1][1:].strip()
        property_state_address, property_zip_address = splitStateZip(property_state_zip_address)
        
        if debug:
            print('state_zip: ' + str(property_state_zip_address))
    
    else: 
        # The city name obtained with the date line is not in the address (probably misspelled) or no city info found
        # Check for street name and add a comma if needed
        
        # Check for street name and see if there is somewhere where we can insert the commas
        street_words = ['AVENUE', 'BOULEVARD', 'CIRCLE', 'COURT', 'DRIVE', 'LANE', 'PLACE', 'ROAD', 'STREET', 'TRAIL',                        'WAY', 'AVE', 'BLVD', 'CIR', 'CT', 'DR', 'LN', 'PL', 'RD', 'ST']

        for street_word in street_words:
            if streetWordInAddress(street_word, property_address):
                property_address = property_address.replace(street_word, street_word + ',')
                break;
        
        # Re-split after adding the ,
        address_words = re.split('\s',property_address) 
        
        if debug:
            print('Property Address after adding , if needed: ', property_address)
            print('Address splits by space: ', str(address_words))
            print('Last split, checking if zip: ', address_words[-1])
        
        zip_re = re.compile('\d{4,6}')
        if len(zip_re.findall(address_words[-1])) > 0:
            # This is the zip, check for the word/s before it if it matches a state
            property_zip_address = address_words[-1].strip()
            property_street_city_state_address = ' '.join(address_words[0:-1])
            
            if debug:
                print('Last split is a zip: ', property_zip_address)
                print('Property Street, City, State Address: ', property_street_city_state_address)
            
            if stateIsInPropertyAddress(property_street_city_state_address):
                property_street_address, property_city_address, property_state_address =                 splitStreetCityStateAddress(property_street_city_state_address)
            else:
                # Error in state - parse using splits
                if debug:
                    print('Last split was a zip but error on state, property_street_city_state_address: ',                           property_street_city_state_address)
                    
                property_street_address, property_city_address, property_state_address, property_zip_address =                 getAddressValuesBasedOnSplits(property_address)
        else: 
            # Last split is either part of a state or a wrong format for zip
            # First check if the last split or last 2 splits correspond to a state
            # If not, try and parse based on splits
            property_street_city_state_address = property_address
            if stateIsInPropertyAddress(property_street_city_state_address):
                # No zip
                # The last split/s correspond to the state
                property_zip_address = ''
                property_street_address, property_city_address, property_state_address =                 splitStreetCityStateAddress(property_street_city_state_address)

            else:
                if debug:
                    print('Last split not a zip, property_street_city_state_address: ', property_street_city_state_address)
                # Error with the zip/state, parse based on ','
                property_street_address, property_city_address, property_state_address, property_zip_address =                 getAddressValuesBasedOnSplits(property_address)
        
    if debug: 
        print('ADDRESSES: ')
        print(property_street_address)
        print(property_city_address)
        print(property_state_address)
        print(property_zip_address)
        
    # Clean the data
    attributes_row[usps_full_address_index] = cleanAddress(property_street_address)
    attributes_row[usps_city_index] = cleanAddress(property_city_address)
    attributes_row[usps_state_index] = getStateCode(cleanAddress(property_state_address))
    attributes_row[usps_zip_index] = cleanZip(property_zip_address)
    
    return attributes_row

def cleanAddress(address):
    address = re.sub('[^A-Za-z0-9#\.,\-&\(\)\s]', '', address)

    return address

def cleanZip(property_zip_address):
    # Convert letters to numbers
    # Remove spaces
    # Only return the first 5 digits
    # If I don't have 5 numbers, return an empty string
    
    zip = property_zip_address.replace(' ', '')
    zip = convertLettersToNumbers(zip)
    if len(zip) >= 5:
        return zip[:5]
    else:
        return ''
    
def stateIsInPropertyAddress(address):
    # This checks if the last word/s hsa the state
    # If the zip is still here, this will return a False
    
    if len(address.strip()) == 0:
        return False
    
    address_words = address.strip().split()
    
    first_state_word_marker_re = re.compile('NEW|NORTH|SOUTH|WEST|RHODE')
    state_name_marker = state_names_list_re.findall(address_words[-1])
     
    # Check for the state
    if address_words[-1][-1] == ',' or address_words[-1][-1] == '.':
        # Remove the comma or period
        address_words[-1] = address_words[-1][:-1]   

    if len(address_words[-1]) == 2 or len(state_name_marker) > 0:
        state_is_here = True
    
    elif len(address_words) > 1 and len(first_state_word_marker_re.findall(address_words[-2])) > 0:
        # State has 2 words
        state_is_here = True
        
    elif len(address_words) > 2 and address_words[-2] == 'OF':
        # State is DC - has 3 words
        state_is_here = True 
    else:
        state_is_here = False
        
    
    return state_is_here

    
def splitStreetCityStateAddress(property_street_city_state_address):
    
    if len(property_street_city_state_address.strip()) == 0:
        return '', '', ''
    
    # Only gets called when state exists (but still added an error-checking in the end just in case)
    address_words = property_street_city_state_address.strip().split()
    
    first_state_word_marker_re = re.compile('NEW|NORTH|SOUTH|WEST|RHODE')
    state_name_marker = state_names_list_re.findall(address_words[-1])
    
    # Check for the state
    if address_words[-1][-1] == ',' or address_words[-1][-1] == '.':
        # Remove the comma or period
        address_words[-1] = address_words[-1][:-1]   

    if len(address_words[-1]) == 2 or len(state_name_marker) > 0:
        state_start_index = len(address_words) - 1
    
    elif len(address_words) > 1 and len(first_state_word_marker_re.findall(address_words[-2])) > 0:
        # State has 2 words
        state_start_index = len(address_words) - 2
            
    elif len(address_words) > 2 and address_words[-2] == 'OF':
        # State is DC - has 3 words
        state_start_index = len(address_words) - 3
        
    else:
        state_start_index = -1
    
    if state_start_index >= 0:
        property_state_address = ' '.join(address_words[state_start_index:])
        if state_start_index > 0:
            property_street_city_address = ' '.join(address_words[0:state_start_index])
            property_street_address, property_city_address = splitStreetCity(property_street_city_address)
        else:
            property_street_address = ''
            property_city_address = ''
            
        if debug:
            print('splitStreetCityStateAddress: Property State Address: ', property_state_address)
            print('splitStreetCityStateAddress: Property Street, City Address: ', property_street_city_address)
    else:
        property_state_address = 'Error on Parsing: ' + property_street_city_state_address
        property_street_address = 'Error on Parsing: ' + property_street_city_state_address
        property_city_address = 'Error on Parsing: ' + property_street_city_state_address

    return property_street_address, property_city_address, property_state_address
        
def splitStateZip(property_state_zip_address):

    address_words = re.split('[\s,]', property_state_zip_address)
    if debug:
        print('splitStateZip: address_words: ', str(address_words))
        
    if len(address_words) > 0:
        # Check first if the last split is a zip and get its index
        zip_re = re.compile('\d{4,6}')
        if len(zip_re.findall(address_words[-1])) > 0:
            zip_marker = zip_re.findall(address_words[-1])[0]
            zip_start_index = property_state_zip_address.find(zip_marker)
            property_zip_address = property_state_zip_address[zip_start_index:zip_start_index+5]
            property_state_address = property_state_zip_address[:zip_start_index-1]
        else:
            # Either error with zip or no zip
            if debug:
                print('splitStateZip: There was an error with zip')
            if stateIsInPropertyAddress(property_state_zip_address):
                state_end_index = len(address_words)
                property_zip_address = ''
            else:
                state_end_index = len(address_words) - 1
                property_zip_address = address_words[-1]
                
            property_state_address = ' '.join(address_words[0:state_end_index])
    else:
        property_state_address = 'Error - no StateZip data'
        property_zip_address = 'Error - no StateZip data'
        
    if debug:
        print('splitStateZip: Property State Address: ', property_state_address)
        print('splitStateZip: Property Zip Address: ', property_zip_address)
    
    return property_state_address, property_zip_address

def splitStreetCity(property_street_city_address):
    if property_street_city_address[-1] == ',' or property_street_city_address[-1] == '.':
        # Remove the , or . at the end
        property_street_city_address = property_street_city_address[:-1]

    addresses = re.split('[,\.]', property_street_city_address.strip())
    # Lots of cases where 'NEW YORK' is not parsed correctly
    new_york_index = property_street_city_address.find('NEW YORK')
    if new_york_index != -1:
        property_city_address = property_street_city_address[new_york_index:].strip()
        property_street_address = property_street_city_address[:new_york_index-1].strip()
    elif len(addresses) >= 2:
        property_street_address = ', '.join(addresses[0:-1]).strip()
        property_city_address = addresses[-1].strip()
    else:
        property_street_address = 'Error in parsing street city:' + property_street_city_address
        property_city_address = 'Error in parsing street city:' + property_street_city_address

    if debug:
        print('splitStreetCity: Property Street Address: ', property_street_address)
        print('splitStreetCity: Property City Address: ', property_city_address)

    return property_street_address, property_city_address


def getAddressValuesBasedOnSplits(property_address):
    
    addresses = property_address.strip().split(',')

    property_street_address = ''
    property_city_address = ''
    property_state_address = ''
    property_zip_address = ''

    if len(addresses) == 4:
        if len(addresses[-1].strip()) >= 4 and len(addresses[-1].strip()) <= 6:
            # Could be one group for street address and state and zip are separated by a comma
            property_street_address = addresses[0].strip()
            property_city_address = addresses[1].strip()
            property_state_address = addresses[2].strip()
            property_zip_address = addresses[3].strip()
            state_zip_together = False
        else:
            # Or 2 groups for street address and state and zip are together
            property_street_address = addresses[0].strip() + ', ' + addresses[1].strip()
            property_city_address = addresses[2].strip()
            property_state_zip_address = addresses[3].strip()
            state_zip_together = True

    elif len(addresses) >= 5:
        # Two or more groups for street address and state and zip could be together or separated
        # If the last split contains only the zip (5 digits), then state and zip are separated
        if addresses[-1].isdigit() or (len(addresses[-1]) >= 4 and len(addresses[-1]) <= 6):
            property_city_address = addresses[-3].strip()
            property_state_address = addresses[-2].strip()
            property_zip_address = addresses[-1].strip()
            state_zip_together = False
            end_street_index = len(addresses) - 4
        else:
            property_city_address = addresses[-2].strip()
            property_state_zip_address = addresses[len(addresses)-1].strip()
            state_zip_together = True
            end_street_index = len(addresses) - 3

        property_street_address = ' '.join(addresses[0:end_street_index])
        
    elif len(addresses) == 3:
        property_street_address = addresses[0].strip()
        property_city_address = addresses[1].strip()
        property_state_zip_address = addresses[len(addresses)-1].strip()
        state_zip_together = True

    elif len(addresses) == 2:
        property_street_address = addresses[0].strip()
        property_city_address = addresses[1].strip()
        if len(property_city_address.strip()) == 0:
            # There's a case where the address was written twice, and if the street address is already filled, the 
            # second address won't be used anymore
            property_street_address = ''
        
        state_zip_together = False
        
    elif len(addresses) == 1:
        property_street_address = ''
        state_zip_together = False
    
    else:
        # Need to look at the address
        property_street_address = 'Error'
        property_city_address = 'Error'
        property_state_address = 'Error'
        property_zip_address = 'Error'
        state_zip_together = False

    if state_zip_together:
        property_state_address, property_zip_address = splitStateZip(property_state_zip_address)

    return property_street_address, property_city_address, property_state_address, property_zip_address
    
def getStateCode(state_name):
    
    if len(state_name.strip()) == 0 or state_name == 'Error':
        return state_name
    
    s= state_name.strip()
    if len(s) == 2:
        if s in state_abbr_list:
            return s
        else:
            return 'Error: State Code does not exist'
    else:
        marker = state_names_list_re.findall(s)
        state_name_index  = 0
        state_marker = ''
        if len(marker) > 0:
            for result in marker[0]:
                if len(result.strip()) > 0:
                    state_marker = result
                    break
                state_name_index += 1

            return state_abbr_list[state_name_index]
        else:
            return 'Error: State name does not match'

    
    
def getParagraph(in_file, start_line, end_marker_re):
    paragraph = start_line.strip()
    next_section_found = False
    new_note_found = False
    end_of_file_found = False        
        
    while not (next_section_found or new_note_found or end_of_file_found):
        line = in_file.readline()
        
        if len(line) == 0:
            end_of_file_found = True
            print('End marker not found: ')
            print(end_marker_re)
            
        elif len(end_marker_re.findall(line)) > 0:
            # There's a CJM file - where the end of a paragraph could not be found
            # Next section is found - this is the end of the paragraph
            next_section_found = True
            if debug:
                print('Paragraph end marker found: ' + str(end_marker_re.findall(line)))
            
#         elif (len(loan_type_re.findall(line)) > 0 or len(arn_re.findall(line)) > 0) and len(line.split()) < 10 \
#         and len(note_to_exclude_re1.findall(line)) == 0 and len(note_to_exclude_re2.findall(line)) == 0:
#             # This is the marker for a new note
#             new_note_found = True
#             if debug:
#                 print('Found a new note marker in line: ', line)
            
        elif len(line.strip()) > 0:
            paragraph = paragraph + ' ' + line.strip()
            
        next_line = line
        
    paragraph = paragraph.strip()
    
    # Replace 3 spaces with just 1
    paragraph = paragraph.replace('   ', ' ').replace('   ', ' ')
    
    if debug:
        print('Paragraph: ')
        print(paragraph)
    
    return paragraph, next_line

def cleanAmount(amount):
    
    if len(amount.strip()) == 0:
        return ''
           
    # This is just used for error messages later
    original_amount = amount
           
    dollar_index = amount.find('$')
    if dollar_index != -1:
        amount = amount[dollar_index+1:].strip()
        if debug:
            print('Amount after removing $: ', amount)
        if amount[0] == ',' or amount[0] == '.' or amount[0] == '0':
            # We are missing a number
            return ('Error - missing the first digit')
    else:
        # If $ does not exist, look at U.S.
        # Sometimes $ becomes an S, 5, 8 or 3.
        # But if the digit is followed by ',', then that digit is part of the amount
        us_marker_re = re.compile('[UuI][\.\si]{0,1}[Ss][\.\si]{0,1}\s{0,}|DOLLARS\s{0,}[Ss]')
        us_marker = us_marker_re.findall(amount)
        if debug:
            print('US marker: ', us_marker)
        if len(us_marker) > 0:
            us_index = amount.find(us_marker[0]) + len(us_marker[0])
            amount = amount[us_index:].strip()
            if debug:
                print('Amount after removing US marker: ', amount)
            # Check if the first character is a 5,3 , or 8. 
            # If it is and the second character is not a',', then remove that digit
            # Otherwise, that digit is part of the number
            digit_dollar_marker_re = re.compile('[Ss358][^,]')
            digit_dollar_marker = digit_dollar_marker_re.findall(amount[:2])
            if len(digit_dollar_marker):
                amount = amount[1:].strip()
                if debug:
                    print('Amount after removing numbers that might have been a dollar sign: ', amount)
            
    
    close_par_index = amount.find(')')
    # There are amounts that are enclosed in ()
    if close_par_index != -1:
        amount_is_enclosed_in_parentheses = True
        amount = amount[:close_par_index].strip()
        if debug:
            print('Amount after removing closing parenthesis: ', amount)
    
    
    open_par_index = amount.find('(') 
    # If this exists, the end marker '(this' has not been caught
    if open_par_index != -1:
        amount = amount[:open_par_index].strip()
        if debug:
            print('Amount to before (: ', amount)
    
    
    end_marker_re = re.compile('and|[oO][rn]')
    end_marker = end_marker_re.findall(amount)
    if len(end_marker) > 0:
        end_index = amount.find(end_marker[0])
        amount = amount[:end_index].strip()
        if debug:
            print('Amount to before \'and\' or \'or\': ', amount)
    
    # Remove the word 'DOLLARS'
    amount = re.sub('(?i)DOLLARS', '', amount)

    if len(amount.strip()) == 0:
        return ''
    
    # Remove these characters from the end of the string
    if amount[-1] == ')' or amount[-1] == ',' or amount[-1] == '.':
        amount = amount[:-1]

    # Convert - to . (there were cases where this is needed)
    amount = amount.replace('-', '.')
    
    # Convert known letters-that-could-be-numbers to numbers
    amount = convertLettersToNumbers(amount)
    
    # If a group of numbers is separated by space, add a','
    # xxx xxx - insert a ,
    cleaning_done = False
    while not cleaning_done:
        amount_re =re.compile('\d{1,3}\s+\d{3}')
        markers = amount_re.findall(amount)
        for marker in markers:
            amount = amount.replace(marker, marker.replace(' ', ','))
        if debug: 
            print('Amount after inserting , between numbers: ', amount)
            
        if len(markers) == 0:
            cleaning_done = True

    # Remove spaces between numbers
    cleaning_done = False
    while not cleaning_done:
        amount_re =re.compile('\d{1,2}\s+\d{1,2}')
        markers = amount_re.findall(amount)
        for marker in markers:
            amount = amount.replace(marker, marker.replace(' ', ''))
        if debug: 
            print('Amount after removing spaces between numbers: ', amount)
            
        if len(markers) == 0:
            cleaning_done = True

    # Remove spaces surrounding commas or dots 
    amount = re.sub('\s{0,},\s{0,}', ',', amount)
    amount = re.sub('\s{0,}\.\s{0,}', '.', amount)
    amount = amount.split()[0]
    
    # Split the number in , or .
    # If the last group has 5 characters - insert a .        
    amount_splits = re.split('[,\.]', amount)
    if debug:
            print('Amount splits: ', str(amount_splits))
    
    if len(amount_splits[-1]) == 5:
        last_split = amount_splits[-1]
        amount_splits[-1] = last_split[:3] + '.' + last_split[-2:]
        amount = ','.join(amount_splits[:])
        if debug:
            print('Need to insert a decimal point: ', last_split)
            print('Amount after inserting decimal point: ', amount)
            
    # Removing everything that is not a number or , or . or a letter - since there is a check if what remains is a digit
    amount = re.sub('[^A-Za-z0-9,\.]', '', amount)
    if debug:
        print('Amount after removing everything that is not a letter, number, . or ,: ', amount)
    
    # Check if this has the right format - the last 3 characters should match (.xx)
    # Check if this has the right format - sometimes the .xx does not exist
    amount_marker_re = re.compile('^\d{1,3}[\.,]\d{3}[\.,]\d{3}[\.,]\d{3}(?:[\.,]\d{2})?|    ^\d{1,3}[\.,]\d{3}[\.,]\d{3}(?:[\.,]\d{2})?|^\d{1,3}[\.,]\d{3}(?:[\.,]\d{2})?|^\d{1,3}(?:[\.,]\d{2})?')
    amount_marker = amount_marker_re.findall(amount)
    
    # If there are numbers with 4 digits or more without spacing, or just 1 number after a . or , -  format is wrong
    wrong_number_re = re.compile('\d{4,}|[,\.]\d{1,2}[,\.]')
    wrong_number_marker = wrong_number_re.findall(amount)
    wrong_decimal_marker_re = re.compile('[,\.]\d')
    wrong_decimal_marker = wrong_decimal_marker_re.findall(amount[-2:])
    
    if debug:
        print('Amount to check: ' + amount)
        print('Markers:')
        print('Amount marker: ', str(amount_marker))
        print('Wrong number marker: ', str(wrong_number_marker))
        print('Wrong decimal marker: ', str(wrong_decimal_marker))
        
    # We need the whole amount and the decimal amount 
    whole_amount = ''
    decimal_amount = ''
    
    # For error checking, there should be at least 4 characters in amount
    if len(amount) >= 4 and len(amount_marker) > 0 and len(wrong_number_marker) == 0     and len(wrong_decimal_marker) == 0:
        if debug:
            print('Amount has right format: ', amount)
            print('Amount marker: ', str(amount_marker))
        decimal_marker_re2 = re.compile('[,\.]\d{2}')
        decimal_marker2 = decimal_marker_re2.findall(amount[-3:])
                
        # There are cases when we get .xxx in the end (this is considered the cents value only when it is a period, not comma)
        # If the last 4 characters are .xxx (this is considered as part of the amount 
        # unless the amount exceeds 900M)
        decimal_marker_re3 = re.compile('\.\d{3}')
        decimal_marker3 = decimal_marker_re3.findall(amount[-4:])

        
        whole_amount = amount
        decimal_amount = ''
        
        if len(decimal_marker2) > 0:
            whole_amount = amount[:-3]   
            decimal_amount = amount[-3:]
            if debug:
                print('Only 2 decimal points for the cents amount')
                print('Amount after separating whole amount with decimal amount: ', whole_amount +'   ' + decimal_amount)
            
        elif (len(decimal_marker3) > 0 and len(amount) > 11):
            whole_amount = amount[:-4]
            decimal_amount = amount[-4:]
            if debug:
                print('There are 3 digita after the decimal point.')
                print('Those are are considered cents if amount is more than $900M')
                print('Those are considered part of the amount if less thatn $900M')
                print('Amount after separating whole amount with decimal amount: ', whole_amount +'   ' + decimal_amount)
          
        
        # Remove all ',' or '.'
        whole_amount = re.sub('[\.,]', '', whole_amount)
        amount = whole_amount + decimal_amount
        amount = amount.replace(',', '.')
        # This makes sure no commas are left but the decimal point - this is needed for rounding
        
        if debug:
            print('Amount after removing all commas in whole amount: ', (whole_amount + decimal_amount))
            
        # Check if everything else that remains are all digits
        if not whole_amount.isdigit():
            amount = 'Error - not digits: ' + original_amount
            if debug:
                print('Amount error: ', amount)
        elif int(whole_amount) < 1000:
            # Return nil if amount is less than 1000
            amount = 'Error - there must be something wrong. Amount is less than 1000: ' + amount
            if debug:
                print('Amount error: ', amount)
        else:
            # Everything is good - do bankers rounding
            float_amount = round(float(amount))
            amount = str(float_amount)
        
    else:
        amount = 'Error on format: ' + original_amount
        if debug:
                print('Amount error: ', amount)
    
    if debug:
        print('Amount to return: ', amount)
        
    return amount


def cleanPercentageNumber(number):
    
    # This is needed for error message
    original_number = number
    
    if len(number.strip()) == 0 or (len(number.strip()) <= 2 and number.isdigit()):
        return number
    
    # Take everything from '(' on:
    open_par_index = number.find('(') 
    # If this exists, the percentage is the number after it
    if open_par_index != -1:
        number = number[open_par_index+1:].strip()
        if debug:
            print('Percentage from ( on : ', number)
        if len(number.strip()) == 0 or (len(number.strip()) <= 2 and number.isdigit()):
            return number
            
    # Remove 'of' and everything below it
    # this is because the marker for the note rate is either 'yearly rate of' or 'yearly rate'    
    if 'of' in number:
        of_index = number.find('of') + 2
        number = number[of_index:].strip()
        if debug:
            print('Percentage after removing anything before \'of\': ', number)
        if len(number.strip()) == 0 or (len(number.strip()) <= 2 and number.isdigit()):
            return number
        
    # Remove . if it is the first/last character in the number
    if number[-1] == '.':
        number = number[:-1]
    if number[0] == '.':
        number = number[1:]
    if debug:
        print('Percentage after removing . :', number)
    
    
    # Remove , if it is the first/last character in the number
    if number[-1] == ',':
        number = number[:-1]
    if number[0] == ',':
        number = number[0:]
    if debug:
        print('Percentage after removing . :', number)
    
    
    # Remove '0/0' - this is badly OCR'd %
    # Replace ',' with .
    # Replace '-' with .
    # Replace .. or ., with just one
    # Remove the spaces
    number = re.sub('0/0|_', '', number)
    number = re.sub('[-,;]', '.', number)
    number = re.sub('[\.,]{2,}', '.', number)
    if debug:
        print('Percentage after changing 0/0 and -_,; : ')
    
    # Replace 'J' with .1
    number = re.sub('J', '.7', number)
    
    # Convert the letters that could be numbers
    number = convertLettersToNumbers(number)
    
    number_marker_re = re.compile('[\d\.\s]+')
    number_marker = number_marker_re.findall(number)
    
    if debug:
        print('Number marker: ', number_marker)
        
    if len(number_marker) > 0:
        number = number_marker[0].strip()
        if number.count('.') == 0 and number.count('\s') == 1:
            number = re.sub('\s', '.', number)
            if debug:
                print('No decimal point and there is one space - replace the space with .: ', number)
        elif number.count('.') == 1:
            number = re.sub(' ', '', number)
            if debug:
                print('One decimal point, remove the spaces', number)
        elif number.count('.') == 0 and len(number.strip()) > 1:
            # No dot, count the number of characters, if there are 5 or more, put the . after the 2 characters.
            # Else, put the . after the first character
            # Remove all spaces
            number = re.sub('\s+', '', number)
            if len(number) >= 5:
                number = number[:2] + '.' + number[2:]
            else:
                number = number[0] + '.' + number[1:]
            if debug:
                print('No decimal point, : ', number)
    
    # Remove everything that is not a space, a number or a .
    number = re.sub('[^0-9\.\s]', '', number)
    if debug:
        print('Percentage after removing everything that is not a number, period, or space: ', number)
    
    # Find x.xxx (2 or 3 decimal places)
    percentage_marker_re = re.compile('\d+\.\d{1,3}')
    percentage_marker = percentage_marker_re.findall(number)
    if debug:
        print('Percentage marker: ', str(percentage_marker))
    
    # Only return up to 3 decimal places
    if len(percentage_marker) > 0:
        number = percentage_marker[0]
    else:
        number = 'Error: Percentage not found: ' + original_number
        
    if debug:
            print('Percentage to return: ', number)
            
    return number

def cleanResetFrequency(freq):
    if len(freq.strip()) == 0:
        return ''
    
    if debug:
        print('Input reset frequency: ', freq)
        
    # Remove 'st', 'nd', 'rd', and 'th'
    ordinal_re_string = '[1liIL:\|\[\]\(\)]st|[2Zz]nd|3rd|[45Ss6G78B90OoDUu]th'
    ordinal_re = re.compile(ordinal_re_string)
    ordinal_marker = ordinal_re.findall(freq)
    if len(ordinal_marker) > 0:
        ordinal_marker_removed = re.sub('st|nd|rd|th', '', ordinal_marker[0])
        freq = freq.replace(ordinal_marker[0], ordinal_marker_removed)
    
    if debug:
        print('Reset frequency after removing ordinal stuff: ', freq)
        
    # Convert known letters-that-could-be-numbers to numbers
    freq = convertLettersToNumbers(freq)
    if debug:
        print('Reset frequency after converting to numbers: ', freq)
            
    # Removing everything that is not a number or , or . or a letter - since there is a check if what remains is a digit
    freq = re.sub('[^0-9]', '', freq)
    if debug:
        print('Reset frequency after removing everything that is not a number: ', freq)
    
    if len(freq) > 2:
        if '12' in freq:
            freq  = '12'
        elif '6' in freq:
            freq = '6'
        else:
            freq = freq[0]

    if debug:
        print('Reset frequency to return: ', freq)

    return freq


def cleanIndex(index):
    
    # Just remove any unreadable characters for now
    index = re.sub('[^A-Za-z0-9\-\.\s,]', '', index)
    
    return index


def cleanLenderName(lender_name):
    
    # Just remove any unreadable characters for now
    lender_name = re.sub('[^A-Za-z0-9\-\.\s,]', '', lender_name)
    
    return lender_name
    
    
def convertLettersToNumbers(number):
    
    if debug:
        print('Original number: ', number)
        
    number = re.sub('[ODoUu]', '0', number)
    number = re.sub('[liIL!\|\[\]\(\)\{\}]', '1', number)
    number = re.sub('[zZ]', '2', number)
    number = re.sub('[sS]', '5', number)
    number = re.sub('G', '6', number)
    number = re.sub('B', '8', number)
    
    if debug:
        print('Converted number: ', number)
    
    return number
    

def processBorrowersPromiseToPayParagraph(paragraph, attributes_row):
    # Extract loan amount and lender
    # 'promise to pay' and 'Lender is" are the start markers
    promise_to_pay_re_string = '[pva]{1,2}.{1,5}[mnrit][unt]{0,1}[iIrl1tun\s][sSn][eoca]s{0,1}\s{0,}' +     '.{0,3}[tiIln\()m][oneua0]{0,1}\s{0,}.{0,3}\s{0,}[pn]{0,1}[aimn]t{0,1}y'
    end_marker_re_string = '.{0,1}t[hI][iulI]s|plus|.Principa[li]|to the order|or so much'
    loan_amount = getValue(paragraph, promise_to_pay_re_string, end_marker_re_string)
    
    if loan_amount.startswith('Error'):
        attributes_row[loan_amount_index] = loan_amount
    else:
        attributes_row[loan_amount_index] = cleanAmount(loan_amount)
        
    
    lender_is_re_string = '[Ll][eac][na][dt][\sl]{0,1}[ecsa].{0,2}[\su]{0,1}[iIl1tra\[][sS583tn]'
    end_marker_re_string = '(?i).thi.|[I1l\|] understand|[I1l\]\[\|].{0,1}[wW][il1t][lit1\]]{2}.make' +     '|\d{0,1}\s{0,}Construction'
    lender_name = getValue(paragraph, lender_is_re_string, end_marker_re_string)
    
    if lender_name.startswith('Error'):
        attributes_row[lender_name_index] = lender_name
    else:
        attributes_row[lender_name_index] = cleanLenderName(lender_name)
    
     
    return attributes_row

def processInterestParagraph(paragraph, attributes_row):
     # Extract original note/interest rate
    yearly_rate_of_re_string = 'ye{0,1}a[rl][l1it]y\s{0,}[rnlTt][aotue][tl]{0,2}[ecn].{0,2}\s{0,}[o0fri]{1,2}' +     '|the\s{0,}[rnl][aotu][tl]{1,2}e.{0,2}\s{0,}[o0fri]{0,2}'
    
    end_marker_re_string =  '\%|[TtIL].{0,1}he'
    note_rate = getValue(paragraph, yearly_rate_of_re_string, end_marker_re_string)
    
    if note_rate.startswith('Error'):
        attributes_row[note_rate_index] = note_rate
        attributes_row[arm_initial_rate_index] = note_rate    
    else:
        attributes_row[note_rate_index] = cleanPercentageNumber(note_rate)
        attributes_row[arm_initial_rate_index] = cleanPercentageNumber(note_rate)
    
        
    return attributes_row


def processPaymentsParagraph(paragraph, attributes_row):
        
    start_marker = time_and_place_of_payments_re.findall(paragraph)
    
    # So far, I have seen the following formats of the PAYMENTS paragraph 
    # where the first section is (A) Time and Place of Payments
    # The paragraphs start with the following
    
    # 1. Beginning on *full date* - this is interest only and the full date follows this text
    # 2. I will pay principal and interest - P&I 
    # 3. "I Will make (my monthly/interest/a) payment/s on the * day of ...  beginning on *full date*" - interest only
    # 4. "I will pay monthly principal and interest
    
    i_will_string = '[Iil1\[\]].{0,3}[WwMmV].{0,1}[iIlt1\|].{1,3}\s{0,}.{0,4}\s{0,}'

    format_re_1_string = '(?i)B[ec].{1,2}[nmt]{2}[lt1iI]{0,1}[nm]g[oant\s]{0,3}\s{0,}'
    format_re_2_string = i_will_string +     '.pay [pP][rn][ilt1]{0,1}n[cCe][iltr1]pa[lit1] and [iIlt][ni]i{0,1}[tli][ecCa][rl]{0,1}.{0,1}[ecm]st'
    format_re_3_string = i_will_string + '.make(a{0,1}|interest|my monthly)\s{0,}pa[yV]\s{0,}ments{0,1}'
    format_re_4_string = i_will_string +     '.pay monthly [pP][rn][ilt1]{0,1}n[cCe][iltr1]pa[lit1] and [iIlt][ni]i{0,1}[tli][ecCa][rl]{0,1}.{0,1}[ecm]st'
    format_re_5_string = 'Pay{0,1}ments During Construction'
    
    format_re_1 = re.compile(format_re_1_string)
    format_re_2 = re.compile(format_re_2_string)
    format_re_3 = re.compile(format_re_3_string)
    format_re_4 = re.compile(format_re_4_string)
    format_re_5 = re.compile(format_re_5_string)
    
    beginning_on_re_string = format_re_1_string + '|commencing\s{0,}[on\s]{0,3}'
    
    first_payment_date_start_marker_re_string = ''
    first_payment_date = ''
    interest_only_exp_date = ''
    maturity_date = ''
    interest_only_at_origination = 'U'
    beginning_text = paragraph[:100]
    
    if len(format_re_1.findall(beginning_text)) > 0:
        # Format 1 - Beginning on *full date* - this is interest only and the full date follows this text
        # Date is after "Beginning on"
        # Interest only at origination
        first_payment_date_start_marker_re_string = format_re_1_string
        interest_only_at_origination = 'Y'

        start_marker_re_string = '[Nn]ote\s{0,}until|[uU]ntil\s{0,}the'
        end_marker_re_string = thereafter_re_string + '|[Oo]n'
        if debug:
            print('This start marker used: ', start_marker_re_string)
            print('This end marker used: ', end_marker_re_string)
            
        interest_only_exp_date = getValue(paragraph, start_marker_re_string, end_marker_re_string)
        if debug:
            print('Format 1 -  Beginning on *full date*')
            
    elif len(format_re_2.findall(beginning_text)) > 0:
        # Format 2 - I will pay principal and interest - P&I 
        # Date is after "beginning on"
        # P&I at origination
        first_payment_date_start_marker_re_string = beginning_on_re_string
        interest_only_at_origination = 'N'
        if debug:
            print('Format 2 - I will pay principal and interest')

    elif len(format_re_3.findall(beginning_text)) > 0:
        # Format 3 -"
        # I Will make (my monthly/interest/a) payment/s on the * day of ...  beginning on *full date*" - interest only
        # Date is after "beginning on"
        # Interest only at origination
        first_payment_date_start_marker_re_string = beginning_on_re_string
        interest_only_at_origination = 'Y'

        start_marker_re_string = 'including (?:\(last .{10,20} date\))?'
        end_marker_re_string = thereafter_re_string + '|[oO]n'
        interest_only_exp_date = getValue(paragraph, start_marker_re_string, end_marker_re_string)

        if debug:
            print('Format 3 - I Will make (my monthly/interest/a) payment/s on the')
            
    elif len(format_re_4.findall(beginning_text)) > 0:
        # Format 4 - "I will pay monthly principal and interest
        # Date is after "beginning on"
        # P&I at origination
        first_payment_date_start_marker_re_string = beginning_on_re_string
        interest_only_at_origination = 'N'
        if debug:
            print('Format 4 - I will pay monthly principal and interest')
    
    elif len(format_re_5.findall(beginning_text)) > 0:
        # Format 5 - 'Construction document'
        first_payment_date_start_marker_re_string = beginning_on_re_string
        interest_only_at_origination = 'Y'
        
        start_marker_re_string = 'including'
        end_marker_re_string = 'My'
        interest_only_exp_date = getValue(paragraph, start_marker_re_string, end_marker_re_string)
        if debug:
            print('Format 5 - Construction file')
        
    else:
        if debug:
            print('Start marker for the formats cannot be found')
        attributes_row[first_payment_date_index] = 'Not found: ' + paragraph[:]
    
    
    first_payment_date_end_marker_re_string = '.Bef[obO][ri][ec] the' + '|' +         'and' + '|' +         'This payment' + '|' + i_will_string
    
    if len(first_payment_date_start_marker_re_string.strip()) > 0:
        first_payment_date = getValue(paragraph, first_payment_date_start_marker_re_string,                                  first_payment_date_end_marker_re_string)
    
    if first_payment_date.startswith('Error'):
        cleaned_date = first_payment_date
        formatted_date = ''
    else:
        cleaned_date, formatted_date = cleanAndFormatDate(first_payment_date)

    attributes_row[first_payment_date_index] = cleaned_date    
    attributes_row[interest_only_at_origination_flag_index] = interest_only_at_origination

    if interest_only_exp_date.startswith('Error'):
        cleaned_date = interest_only_exp_date
        formatted_date = ''
    else:
        cleaned_date, formatted_date = cleanAndFormatDate(interest_only_exp_date)

    attributes_row[interest_only_exp_date_index] = cleaned_date

        
    # Get the maturity date
    maturity_date_start_marker_re_string = '(?i)[ILFT]{2},{0,1}\s{0,}o[nh]'
    maturity_date_end_marker_re_string = '(?i)[I1LT\|]\s{0,}[Ss5][til1\|]{3,5}'
    maturity_date = getValue(paragraph, maturity_date_start_marker_re_string, maturity_date_end_marker_re_string)
    # If maturity date can't be found due to the marker "If, on" is not found 
    # Some files only say "On (insert date here), which is called the Maturity date
    # Use the interest_only_exp_date or first_payment_date as the marker, whichever is around
    if maturity_date.startswith('Error: Start') or maturity_date.startswith('Error: None'):
        if debug:
            print('The original \'If on\' marker for maturity date is not found')
        if not interest_only_exp_date.startswith('Error'):
            new_marker_re = re.compile(interest_only_exp_date + '(.*)' + 'which')
            new_maturity_date = new_marker_re.findall(paragraph)
            if debug:
                print('Interest only exp date exists so this is used as a marker')
                print('New maturity date marker: ', new_maturity_date)
            
            if len(new_maturity_date) > 0:
                maturity_date = new_maturity_date[0]
                if debug:
                    print('New maturity date: ', new_maturity_date)
            
    if maturity_date.startswith('Error'):
        cleaned_date = maturity_date
        formatted_date = ''
    else:
        cleaned_date, formatted_date = cleanAndFormatDate(maturity_date)
        
    attributes_row[maturity_date_index] = cleaned_date
    
    # Get the amount of initial monthly payments
    monthly_payment_amount_start_marker_re_string = 'will be in the amount of'
    monthly_payment_amount_end_marker_re_string = thereafter_re_string + '|before|This amount'
    monthly_payment_amount = getValue(paragraph, monthly_payment_amount_start_marker_re_string,                                      monthly_payment_amount_end_marker_re_string)
    attributes_row[pi_amount_index] = monthly_payment_amount
    
    
    return attributes_row


def processInterestRateAndPaymentChangesParagraph(paragraph, attributes_row):
    change_dates_re_string = 'Change\s{0,}Dates'
    index_re_string = '[TtlL]h.\s{0,}.{0,2}[TIil\s][nri\s]{1,2}[dmicl\s]{1,2}[ce].{1,3}' +    '(?:.{0,2}\s{0,}[\[iI1l][sS58].{0,1}\s{0,}[tTL]{0,1}[hH][eE])?'
    calculation_re_string  = 'Calculation|Interest Rate Change'
    limits_on_interest_re_string = '[Ll]imits\s{0,}[oa]n\s{0,}[Ii]nterest|Interest\s{0,}Rate\s{0,}[Ll]imit'
    effective_date_or_notice_string = 'Payment\s{0,}Change\s{0,}Dates|Effective\s{0,}Date|Noti.{1,3}\s{0,}of\s{0,}Changes'
    
    change_dates_paragraph = getValue(paragraph, change_dates_re_string, index_re_string)
    if not change_dates_paragraph.startswith('Error'):
        change_date_start_marker_re_string = '\s{1,}[Oo]n\s{1,}[the]{0,3}'
        change_date_end_marker_string = '\s{1,}[ao]nd\s{1,}|\s{1,}[oa]n\s{1,}' + '|' + thereafter_re_string
        change_date = getValue(change_dates_paragraph, change_date_start_marker_re_string, change_date_end_marker_string)
        if change_date.startswith('Error'):
            cleaned_date = change_date
            formatted_date = ''
        else:
            cleaned_date, formatted_date = cleanAndFormatDate(change_date)
        attributes_row[change_date_index] = cleaned_date

        if attributes_row[interest_only_at_origination_flag_index] == 'Y' and         len(attributes_row[interest_only_exp_date_index]) == 0:
            # It is interest only at origination and no interest expiry date in the paragraph. 
            # Use the change date
            attributes_row[interest_only_exp_date_index] = cleaned_date

        pmt_reset_freq_start_marker_re_string = '[ec]v[ec]ry'
        pmt_reset_freq_end_marker_re_string = '[mM][oO0]n[lti]h'
        payment_reset_frequency = getValue(change_dates_paragraph, pmt_reset_freq_start_marker_re_string,                                           pmt_reset_freq_end_marker_re_string)

        if payment_reset_frequency.startswith('Error'):
            # Try finding for year
            pmt_reset_freq_end_marker_re_string = 'year'
            payment_reset_frequency = getValue(change_dates_paragraph, pmt_reset_freq_start_marker_re_string,                                           pmt_reset_freq_end_marker_re_string)
            if payment_reset_frequency.startswith('Error'):
                attributes_row[arm_payment_reset_freq_index] = payment_reset_frequency
            else:
                if len(payment_reset_frequency.strip()) == 0:
                    attributes_row[arm_payment_reset_freq_index] = '12' # 1 year
                else:
                    attributes_row[arm_payment_reset_freq_index] = str(12 * int(cleanResetFrequency(payment_reset_frequency)))

        else:
            if len(payment_reset_frequency.strip()) == 0:
                attributes_row[arm_payment_reset_freq_index] = '1'
            else:
                attributes_row[arm_payment_reset_freq_index] = cleanResetFrequency(payment_reset_frequency)
    else:
        # Change Dates paragraph not found
        attributes_row[change_date_index] = 'Error: Change Dates paragraph not found'
        attributes_row[arm_payment_reset_freq_index] = 'Error: Change Dates paragraph not found'
                
    index_paragraph = getValue(paragraph, index_re_string, calculation_re_string)
    if not index_paragraph.startswith('Error'):
        index_start_marker_re_string = index_re_string
        index_end_marker_re_string = '(?i)[T\[]h[eco]\s{0,}.{0,2}\s{0,}[mrni]{1,2}[oei]{1,2}\s{0,1}st'
        index_info = getValue(index_paragraph, index_start_marker_re_string, index_end_marker_re_string)
        if index_info.startswith('Error'):
            attributes_row[arm_index_index] = index_info
        else:
            attributes_row[arm_index_index] = cleanIndex(index_info)
    else:
        # Index paragraph not found
        attributes_row[arm_index_index] = 'Error: Index paragraph not found'
    

    calculation_of_changes_paragraph = getValue(paragraph, calculation_re_string, limits_on_interest_re_string)
    if not calculation_of_changes_paragraph.startswith('Error'):
        margin_rate_start_marker_re_string = 'percent(?:[as]\s{0,1}g[ew]\s{0,}'+        '[pP][oO0a\s][inm1lIH]{1,3}[tmL]\({0,1}.{0,1}\){0,1})?\s{0,}.'
        margin_rate_end_marker_re_string = '\%|to the'
        arm_margin_at_origination = getValue(calculation_of_changes_paragraph, margin_rate_start_marker_re_string,                                              margin_rate_end_marker_re_string)
        if arm_margin_at_origination.startswith('Error'):
            attributes_row[arm_margin_at_origination_index] = arm_margin_at_origination
        else:
            attributes_row[arm_margin_at_origination_index] = cleanPercentageNumber(arm_margin_at_origination)
    
    else:
        # Calculation of Changes paragraph not found
        attributes_row[arm_margin_at_origination_index] = 'Error: Calculation of Changes paragraph not found'
    
    # Get Limits paragraph
    limits_paragraph = getValue(paragraph, limits_on_interest_re_string, effective_date_or_notice_string)
    if not limits_paragraph.startswith('Error'):
        periodic_rate_cap_start_marker_re_string = '[m\s]ore\s{0,}than'
        periodic_rate_cap_end_marker_re_string = 'p{0,1}[ec]{0,1}r[ce]{2}nt[as]\s{0,1}g[ewc]{0,1}|%|from\s{0,}the' +         '|' + thereafter_re_string
        periodic_rate_cap = getValue (limits_paragraph, periodic_rate_cap_start_marker_re_string,                                      periodic_rate_cap_end_marker_re_string)
        if periodic_rate_cap.startswith('Error') or len(periodic_rate_cap.strip()) == 0:
            attributes_row[arm_periodic_rate_cap_index] = periodic_rate_cap
        else:
            periodic_rate_cap = periodic_rate_cap.lower().strip()
            periodic_rate_cap = periodic_rate_cap.split()[0]
            periodic_rate_cap_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
            try:
                periodic_rate_cap_number = periodic_rate_cap_words.index(periodic_rate_cap)
                attributes_row[arm_periodic_rate_cap_index] = str(periodic_rate_cap_number)
                attributes_row[arm_periodic_rate_floor_index] = str(periodic_rate_cap_number)
            except ValueError:
                attributes_row[arm_periodic_rate_cap_index] = 'Error: Cannot find periodic rate cap'
                attributes_row[arm_periodic_rate_floor_index] = 'Error: Cannot find periodic rate cap'        

        greater_than_re_string = 'g[rmi].{1,2}[tm][ea][rit]\s{0,}.h[ae]n'
        less_than_re_string = '[lerao]{1,2}[su]{2}\s{0,}th[ae]n'
        never_be_greater_than_re_string = 'never\s{0,}be\s{0,1}' + greater_than_re_string +'(?:.{,50}p[o)O][iltI]n[tliI]s)?'
        not_be_greater_than_re_string = 'not\s{0,}be\s{0,1}' + greater_than_re_string
        lifetime_rate_ceiling_start_marker_re_string = never_be_greater_than_re_string +        '|never\s{0,}increase\s{0,}to\s{0,}more\s{0,}than'+ '|lesser\s{0,}of'
        lifetime_rate_ceiling_end_marker_re_string = '\%|[wW]hic[hl]{1,2}|or' + '|' + thereafter_re_string
        lifetime_rate_ceiling = getValue(limits_paragraph, lifetime_rate_ceiling_start_marker_re_string,                                        lifetime_rate_ceiling_end_marker_re_string)
                                            
        if lifetime_rate_ceiling.startswith('Error: Start'):
            # Try not_be_greater_than
            lifetime_rate_ceiling_start_marker_re_string = not_be_greater_than_re_string
            lifetime_rate_ceiling = getValue(limits_paragraph, lifetime_rate_ceiling_start_marker_re_string,                                        lifetime_rate_ceiling_end_marker_re_string)
            if lifetime_rate_ceiling.startswith('Error'):
                # Still error
                attributes_row[arm_lifetime_rate_ceiling_index] = lifetime_rate_ceiling
            else:
                attributes_row[arm_lifetime_rate_ceiling_index] = cleanPercentageNumber(lifetime_rate_ceiling)
        else:
            attributes_row[arm_lifetime_rate_ceiling_index] = cleanPercentageNumber(lifetime_rate_ceiling)
        
        
        lifetime_rate_floor_start_marker_re_string = never_be_greater_than_re_string + '.*or\s{0,}' + less_than_re_string +          '|no event\s{0,}' + less_than_re_string + '|lesser of.*' + less_than_re_string
        lifetime_rate_floor_end_marker_re_string = '[\%\(\)]' + '|' + thereafter_re_string
        lifetime_rate_floor = getValue(limits_paragraph, lifetime_rate_floor_start_marker_re_string,                                       lifetime_rate_floor_end_marker_re_string)
        if lifetime_rate_floor.startswith('Error: Start'):
            # Try not_greater_than
            lifetime_rate_floor_start_marker_re_string = not_be_greater_than_re_string +  '.*or\s{0,}' + less_than_re_string
            lifetime_rate_floor = getValue(limits_paragraph, lifetime_rate_floor_start_marker_re_string,                                       lifetime_rate_floor_end_marker_re_string)
            if lifetime_rate_floor.startswith('Error'):
                attributes_row[arm_lifetime_rate_floor_index] = lifetime_rate_floor
            else:
                attributes_row[arm_lifetime_rate_floor_index] = cleanPercentageNumber(lifetime_rate_floor)
        else:
            attributes_row[arm_lifetime_rate_floor_index] = cleanPercentageNumber(lifetime_rate_floor)
        
        lifetime_rate_ceiling = attributes_row[arm_lifetime_rate_ceiling_index]
        lifetime_rate_floor = attributes_row[arm_lifetime_rate_floor_index]
        if not lifetime_rate_ceiling.startswith('Error')and not lifetime_rate_floor.startswith('Error')         and len(lifetime_rate_ceiling.strip()) > 0 and len(lifetime_rate_floor.strip()) > 0:
            # Check if rate_ceiling < rate_floor
            # There might be an issue with the decimal point for ceiling (since we always put it after the first digit)
            if debug:
                print('The rate ceiling and floor have values: ', float(lifetime_rate_ceiling), float(lifetime_rate_floor))
            if float(lifetime_rate_ceiling) < float(lifetime_rate_floor):
                if debug:
                    print('Lifetime rate ceiling is less than lifetime rate floor: ', lifetime_rate_ceiling, lifetime_rate_floor)
                lifetime_rate_ceiling = lifetime_rate_ceiling.replace('.', '')
                if len(lifetime_rate_ceiling) > 2:
                    lifetime_rate_ceiling = lifetime_rate_ceiling[:2] + '.' + lifetime_rate_ceiling[2:]
                
                if debug:
                    print('New lifetime rate ceiling: ', lifetime_rate_ceiling)
                attributes_row[arm_lifetime_rate_ceiling_index] = lifetime_rate_ceiling
                
        # Compute for ARM Lifetime Rate Cap
        lifetime_rate_ceiling = attributes_row[arm_lifetime_rate_ceiling_index]
        lifetime_rate_floor = attributes_row[arm_lifetime_rate_floor_index]
        if lifetime_rate_ceiling.startswith('Error') or lifetime_rate_floor.startswith('Error')         or len(lifetime_rate_ceiling.strip()) == 0 or len(lifetime_rate_floor.strip()) == 0:
            attributes_row[arm_lifetime_rate_cap_index] =  'Error: cannot compute for lifetime rate cap index' +            ' (either empty or error)'
        else:
            arm_lifetime_rate_cap = str(float(lifetime_rate_ceiling) - float(lifetime_rate_floor))
            # Only get upto 3 decimal places
            # Find the .
            decimal_point_index = arm_lifetime_rate_cap.find('.')
            if decimal_point_index > 0:
                attributes_row[arm_lifetime_rate_cap_index] =  arm_lifetime_rate_cap[:decimal_point_index+3]
            else:
                attributes_row[arm_lifetime_rate_cap_index] =  arm_lifetime_rate_cap

    else:
        # Limits paragraph not found
        attributes_row[arm_periodic_rate_cap_index] = 'Error: Limits paragraph not found'
        attributes_row[arm_periodic_rate_floor_index] = 'Error: Limits paragraph not found'
        attributes_row[arm_lifetime_rate_floor_index] = 'Error: Limits paragraph not found'
        attributes_row[arm_lifetime_rate_ceiling_index] = 'Error: Limits paragraph not found'

    return attributes_row


def processBorrowersRightToPrepayParagraph(paragraph, attributes_row):

    prepayment_marker_re_string =     '(If\s{0,}I\s{0,}make\s{0,}a\s{0,}full\s{0,}[Pp]repayment\s{0,}or\s{0,}[a\s]{0,}partial\s{0,}' +    '[pP]repayments{0,1}\s{0,}within\s{0,}(.*)\s{0,}from\s{0,}today,{0,1}\s{0,}I\s{0,}will\s{0,}pay\s{0,}' +     'Lender\s{0,}a\s{0,}[pP]repayment\s{0,}charge\s{0,}equal\s{0,}to\s{0,}(.*)\s{0,}percent\s{0,}of\s{0,}' +     'the\s{0,}amount\s{0,}of\s{0,}the\s{0,}[pP]repayment)'
    
    no_penalty_marker_re_string =     '((After .*)?[Il]\s{0,}may.{0,2}\s{0,}make\s+a\s+full\s{0,}([pP]repayment)?\s{0,}or\s{0,}partial\s{0,}' +     '[pP]repayments{0,1}\s{0,}without\s{0,}(having\s{0,}to\s{0,}pay|paying)\s{0,}(a|any)\s{0,}[pP]repayment charge)'
    
    prepayment_marker_re = re.compile(prepayment_marker_re_string)
    no_penalty_marker_re = re.compile(no_penalty_marker_re_string)
    
    prepayment_marker = prepayment_marker_re.findall(paragraph)
    no_penalty_marker = no_penalty_marker_re.findall(paragraph)
    
    if len(no_penalty_marker) > 0:
        if len(prepayment_marker) > 0:
            attributes_row[prepayment_penalty_flag_index] = 'Y'
            attributes_row[prepayment_penalty_term_index] = prepayment_marker[0][1]
        elif len(no_penalty_marker[0][1].strip()) == 0:
            attributes_row[prepayment_penalty_flag_index] = 'N'
            attributes_row[prepayment_penalty_term_index] = '0'
        else:
            attributes_row[prepayment_penalty_flag_index] = 'Error: Prepayment Penalty Markers not found ' +  paragraph
            attributes_row[prepayment_penalty_term_index] = 'Error'
        
    else:
        attributes_row[prepayment_penalty_flag_index] = 'Error: Prepayment Penalty Markers not found ' + paragraph
        attributes_row[prepayment_penalty_term_index] = 'Error'
        
    if debug:
        print('Prepayment marker: ')
        print(prepayment_marker)
        print('No penalty marker: ')
        print(no_penalty_marker)

    
    return attributes_row
    

# def getValue(paragraph, start_re_string, end_re_string):
    
#     marker_string = '(' + start_re_string + ')(.*)(' + end_re_string + ')'
#     print('Marker string: ', marker_string)
#     marker_re = re.compile(marker_string)
    
#     marker = marker_re.findall(paragraph)
#     if len(marker) > 0 and len(marker[0]) > 1:
#         value = marker[0][1]
#     else:
#         value = 'Not found: ' + paragraph
    
#     if debug:
#         print('Marker re: ', marker_re)
#         print('Marker: ', marker)
#     return value


def getValue(paragraph, start_re_string, end_re_string):
    
    start_re = re.compile(start_re_string)
    end_re = re.compile(end_re_string)
    
    start_marker = start_re.findall(paragraph)
    end_marker = end_re.findall(paragraph)
 
    # There are cases when the markers will return more than 1 results
    # We are using the first result
    paragraph_to_search = paragraph
    if len(start_marker) > 0 and len(end_marker) > 0:
        start_index = paragraph_to_search.find(start_marker[0]) + len(start_marker[0])
        end_index = 0
        for em in end_marker:
            # This makes sure that even when we have multiple results of the same exact string,
            # the code only gets the one where end_index > start_index
            search_end_index = paragraph_to_search.find(em)
            end_index += search_end_index
            if debug:
                print('Start index for marker: ' + str(start_index) + ' ' + start_marker[0])
                print('End index for marker: ' +  str(end_index) + ' ' + em)
            if end_index >= start_index + 1:
                break;
            else:
                search_end_index += len(em)
                end_index += len(em)
                paragraph_to_search = paragraph_to_search[search_end_index:]
            
        value = paragraph[start_index:end_index].strip()
        
    elif len(end_marker) > 0:
        start_index = -1
        end_index = paragraph.find(end_marker[0])
        value = 'Error: Start marker not found: ' + paragraph.strip()
        
    elif len(start_marker) > 0:
        start_index = paragraph.find(start_marker[0]) + len(start_marker[0])
        end_index = -1
        value = 'Error: End marker not found: ' + paragraph[start_index:].strip()
    
    else:
        start_index = -1
        end_index = -1
        value = 'Error: None of the markers found: ' + paragraph
    
    if debug:
        print('Value: ', value)
        print('Start marker: ', str(start_marker), start_re)
        print('End marker: ', str(end_marker), end_re)
        print('Start index: ', str(start_index))
        print('End index: ', str(end_index))
        
    return value

def computeForMonthsDifference(date1, date2):
    # Assumption is date is in format Months Day, Year
    if date1.startswith('Error') or date2.startswith('Error') or len(date1.strip()) == 0 or len(date2.strip()) == 0:
        return 'Error: cannot compute for months. One or both dates are empty/with error.'
    
    date1_splits = date1.split()
    date2_splits = date2.split()
    
    year1 = int(date1_splits[2])
    month1 = clean_months.index(date1_splits[0]) + 1
    day1 = date1_splits[1]
    
    year2 = int(date2_splits[2])
    month2 = clean_months.index(date2_splits[0]) + 1
    day2 = date2_splits[1]
    
    
    # Make sure date1 is more recent than date2 so # of months = date1 - date2
    if year1 < year2 or (year1 == year2 and month1 < month2):
        # Switch dates
        temp = year1
        year1 = year2
        year2 = temp
        
        temp = month1
        month1 = month2
        month2 = temp
        
        temp = day1
        day1= day2
        day2 = temp
        

    # Compute for the difference in months:
    return str(12 * (year1 - year2) + (month1 - month2))
    

def extractNoteAttributes(file):
    
    # There are CJM documents with multiple notes in one file
    multiple_attributes_rows = []
    attributes_row = [''] * len(notes_header)
   
    # How to check if file does not exist
    in_file = open(file, 'r')
    
    done = False
    
    # Finding paragraphs
    borrowers_promise_to_pay_paragraph_found = False
    interest_paragraph_found = False
    payments_paragraph_found = False
    interest_rate_and_payment_changes_paragraph_found = False
    borrowers_right_to_prepay_paragraph_found = False
    
    previous_lines = ['', '', ''] # Sometimes the address has 3 lines
    next_line = ''
    
    line_with_date = ''
    mortgage_date = ''
    
    notes = []
    while not done:
        
        if len(next_line.strip()) > 0:
            line = next_line
            if debug:
                print('next line: ' + next_line)
        else:
            line = in_file.readline()
        
        next_line = ''
        
        if len(line) == 0:
            # End of file
            in_file.close()
            print('End of file')
            done = True
        
        line = line.strip()
        if len(line) < 3:
            # This is an empty line
            continue
            
        
        only_letters = ''.join(re.findall('[a-zA-Z]+', line))
        letter_count = len(only_letters)
        paragraph = ''
        
        # This is used for checking the date marker (it has to be on the first split)
        line_splits = re.split(r'\s{10,}', line)

        
        if len(loan_type_re.findall(line)) > 0 and len(addendum_re.findall(line)) == 0         and len(allonge_re.findall(line)) == 0 and 'THIS' not in line and         not borrowers_promise_to_pay_paragraph_found:
            # No addendums (for now)
            # Get the loan type and payment type (if loan type is empty)
            if debug:
                print('Found the initial loan type in line: ', line)
                
            attributes_row = getLoanAndPaymentTypes(line, previous_lines[1], attributes_row, in_file)
                
        elif len(date_re.findall(line)) > 0 or (len(city_re.findall(line))  > 0 and len(state_re.findall(line)) > 0)        and len(attributes_row[mortgage_date_index].strip()) == 0 and not borrowers_promise_to_pay_paragraph_found:
            # Looking for [Date], [City], [State] - at least we should have 2
            # Date should be in the first split
            if debug:
                print('Found date marker. Previous lines: ' + str(date_re.findall(line)) + ' + ' +                       str(city_re.findall(line)) + ' + ' + str(state_re.findall(line)) + ' + ' + str(previous_lines))
            attributes_row = getDateAndCity(line, previous_lines, attributes_row)
            previous_lines = ['', '', '']
            
            
        elif len(property_address_re.findall(line)) > 0 and len(attributes_row[usps_full_address_index].strip()) == 0        and not borrowers_promise_to_pay_paragraph_found:
            # Found [Property Address] and address information is not available yet
            if debug:
                print('Found property address marker: ' + line)
            
            # Check if a colon follows the marker. If so, address is right next to the marker and the line below (if not empty)
            # Otherwise, address information is above
            property_address_marker = property_address_re.findall(line)
            if debug:
                print('Property Address marker: ', str(property_address_marker))
            colon_index = line.find(':')
            if colon_index > line.find(property_address_marker[0]) and colon_index < len(line):
                if debug: 
                    print("Property address marker found with colon")
                next_address_line_found = False
                while not next_address_line_found:
                    next_line = in_file.readline().strip()
                    if len(next_line) > 0:
                        next_address_line_found = True
                        property_address = line[colon_index+1 :].strip() + ', ' + next_line
            
                property_address = property_address.strip()
                if property_address[0] == ',':
                    # Remove the , in the beginning
                    property_address = property_address[1:]
                    
            else:
                # The address could be upto 3 previous lines
                property_address = getPropertyAddressFromLines(previous_lines, line_with_date)
            
            if debug:
                print('Property address to parse: ', property_address)
            # Get address values and get the date too (if the information is not in attributes_row yet)
            if len(property_address.strip()) > 0:
                attributes_row = getAddressValues(property_address, attributes_row)
            if len(line_with_date.strip()) > 0 and len(attributes_row[mortgage_date_index].strip()) == 0: 
                mortgage_date = getMortgageDate(line_with_date)
                cleaned_date, formatted_date = cleanAndFormatDate(mortgage_date)
                attributes_row[mortgage_date_index] = cleaned_date
                attributes_row[productions_fund_date_index] = cleaned_date
                line_with_date = ''

                
        elif len(borrowers_promise_to_pay_re.findall(line)) > 0 and not borrowers_promise_to_pay_paragraph_found        and not 'FOR VALUE RECEIVED' in line:
            # Found 'BORROWER'S PROMISE TO PAY
            borrowers_promise_to_pay_end_marker_re_string = interest_uc_re_string + '|' + interest_lc_re_string +              '|' +  payments_re_string + '|' + time_and_place_of_payments_re_string +                  '|' + interest_rate_and_payment_changes_re_string + '|' + change_dates_re_string +                '|' + loan_charges_re_string
                
            borrowers_promise_to_pay_end_marker_re = re.compile(borrowers_promise_to_pay_end_marker_re_string)
            
            if debug:
                print('Marker found :', str(borrowers_promise_to_pay_re.findall(line)))
                print('Found BORROWER\'S PROMISE TO PAY in line: ' + line)
                print('End marker: ' + str(borrowers_promise_to_pay_end_marker_re))
            
            # Get the BORROWER'S PROMISE TO PAY PARAGRAPH
            paragraph, next_line = getParagraph(in_file, line, borrowers_promise_to_pay_end_marker_re)
            borrowers_promise_to_pay_paragraph_found = True
            
            attributes_row = processBorrowersPromiseToPayParagraph(paragraph, attributes_row)
            
            # There are cases where the date, property address, and loan information are still not resolved, so extract them here
            if len(attributes_row[loan_type_index].strip()) == 0:
                # Loan type not yet found
                attributes_row[loan_type_index] = 'NOTE'
            
            if len(attributes_row[usps_full_address_index].strip()) == 0:
                property_address = getPropertyAddressFromLines(previous_lines, line_with_date)
                
                if len(property_address.strip()) > 0:
                    attributes_row = getAddressValues(property_address, attributes_row)
                    if debug:
                        print('Addresses saved in attributes row: ' + property_address)
            
            if len(line_with_date.strip()) > 0 and len(attributes_row[mortgage_date_index].strip()) == 0:
                mortgage_date = getMortgageDate(line_with_date)
                cleaned_date, formatted_date = cleanAndFormatDate(mortgage_date)
                attributes_row[mortgage_date_index] = cleaned_date
                attributes_row[productions_fund_date_index] = cleaned_date
                line_with_date = ''
                if debug:
                    print('Date saved in attributes row: ' + attributes_row[mortgage_date_index])

            
        elif ((len(interest_uc_re.findall(line)) > 0 and letter_count <= 10 ) or len(interest_lc_re.findall(line)) > 0)         and not interest_paragraph_found and borrowers_promise_to_pay_paragraph_found:
            # If all upper case INTEREST - it should only have less than 10 characters/letters
            
             # Get the INTEREST paragraph
            interest_end_marker_re_string = payments_re_string + '|' + time_and_place_of_payments_re_string +              '|' + interest_rate_and_payment_changes_re_string + '|' + change_dates_re_string +             '|' + borrowers_right_to_prepay_re_string + '|' + loan_charges_re_string
            interest_end_marker_re = re.compile(interest_end_marker_re_string)
            
            if debug:
                print('Found INTEREST in line: ' + line)
                
            paragraph, next_line = getParagraph(in_file, line, interest_end_marker_re)
            interest_paragraph_found = True
            
            attributes_row = processInterestParagraph(paragraph, attributes_row)
            
                
        elif (len(payments_re.findall(line)) > 0 or len(time_and_place_of_payments_re.findall(line)) > 0)        and not payments_paragraph_found and borrowers_promise_to_pay_paragraph_found:
            # Get the PAYMENTS paragraph
            # The next paragraph is either INTEREST RATE AND.*PAYMENT CHANGES or BORROWER'S RIGHT TO PREPAY
            payments_end_marker_re_string = interest_rate_and_payment_changes_re_string + '|' + change_dates_re_string +             '|' + borrowers_right_to_prepay_re_string + '|' + loan_charges_re_string
            payments_end_marker_re = re.compile(payments_end_marker_re_string)
            
            if debug:
                print('Found PAYMENTS/Time and Place of Payments in line: ' + line)
                
            paragraph, next_line = getParagraph(in_file, line, payments_end_marker_re)
            payments_paragraph_found = True
            
            attributes_row = processPaymentsParagraph(paragraph, attributes_row)
            
            
        elif (len(interest_rate_and_payment_changes_re.findall(line)) > 0 or len(change_dates_re.findall(line)) > 0)         and not interest_rate_and_payment_changes_paragraph_found and borrowers_promise_to_pay_paragraph_found: 
            
            interest_rate_and_payment_changes_end_marker_re_string = borrowers_right_to_prepay_re_string +             '|' + loan_charges_re_string
            interest_rate_and_payment_changes_end_marker_re = re.compile(interest_rate_and_payment_changes_end_marker_re_string)
            
            if debug:
                print('Found INTEREST RATE AND PAYMENT CHANGES/Change Dates in line: ' + line)
                
            paragraph, next_line = getParagraph(in_file, line, interest_rate_and_payment_changes_end_marker_re)
            interest_rate_and_payment_changes_paragraph_found = True
            
            attributes_row = processInterestRateAndPaymentChangesParagraph(paragraph, attributes_row)
            
            
        elif len(borrowers_right_to_prepay_re.findall(line)) > 0         and not borrowers_right_to_prepay_paragraph_found and borrowers_promise_to_pay_paragraph_found:
            
            borrowers_right_to_prepay_end_marker_re_string = loan_charges_re_string
            borrowers_right_to_prepay_end_marker_re = re.compile(borrowers_right_to_prepay_end_marker_re_string)
            
            if debug:
                print('Found BORROWERS RIGHT TO PREPAY in line: ' + line)
                
            paragraph, next_line = getParagraph(in_file, line, borrowers_right_to_prepay_end_marker_re)
            borrowers_right_to_prepay_paragraph_found = True
            
            attributes_row = processBorrowersRightToPrepayParagraph(paragraph, attributes_row)
            
            # NOTE: Change this - some files have multiple Notes so change this to resetting the attributes_row
            done = True
            
        elif len(loan_charges_re.findall(line)) > 0 and borrowers_promise_to_pay_paragraph_found:
            done = True

        else:
            # We save the last 3 non-empty lines
            # Some addresses have 3 lines
            previous_lines[0] = previous_lines[1]
            previous_lines[1] = previous_lines[2]
            previous_lines[2] = line
            

        if not done and not borrowers_promise_to_pay_paragraph_found:
            # If line has the mortgage date and BORROWER'S PROMISE TO PAY is not found yet, get this date 
            # We always want the most recent date closest to the paragraph
            # Remove this line from previous_lines
            
            if len(getMortgageDate(line).strip()) > 0:
                line_with_date = line
            
                previous_lines = ['', '', '']
                if debug:
                    print('Found line with date: ' + line_with_date)
            
    
    in_file.close()
    
    # Add the computed number of months
    mortgage_date = attributes_row[mortgage_date_index]
    change_date = attributes_row[change_date_index]
    interest_only_exp_date = attributes_row[interest_only_exp_date_index]
    maturity_date = attributes_row[maturity_date_index]
    
    attributes_row[initial_rate_period_index] = computeForMonthsDifference(change_date, mortgage_date)
    attributes_row[interest_only_term_index] = computeForMonthsDifference(interest_only_exp_date, mortgage_date)
    attributes_row[loan_term_index] = computeForMonthsDifference(maturity_date, mortgage_date)
    
    # Add the paragraphs not found for this document
    paragraphs_not_found = ''
    if borrowers_promise_to_pay_paragraph_found == False:
        paragraphs_not_found = paragraphs_not_found + 'No Borrowers Promise to Pay Paragraph + '
    if interest_paragraph_found == False:
        paragraphs_not_found = paragraphs_not_found + 'No Interest Paragraph + '
    if payments_paragraph_found == False:
        paragraphs_not_found = paragraphs_not_found + 'No Payments Paragraph + '
    if interest_rate_and_payment_changes_paragraph_found == False:
        paragraphs_not_found = paragraphs_not_found + 'No Interest Rate and Payment Changes Paragraph +'
    if borrowers_right_to_prepay_paragraph_found == False:
        paragraphs_not_found = paragraphs_not_found + 'No Borrowers Right to Prepay Paragraph +'
    attributes_row[paragraphs_not_found_index] = paragraphs_not_found
    
    if debug: 
        print('Attributes row: ', str(attributes_row))
    
    # This clears out every attribute that starts with 'Error' - if set to True
    clean_output = True
    if clean_output:
        attribute_index = 0
        while attribute_index < len(attributes_row):
            attribute = attributes_row[attribute_index]
            if debug:
                print('Attribute + index: ', attribute + ' ' + str(attribute_index))
            if attribute.startswith('Error'):
                attributes_row[attribute_index] = ''
            attribute_index += 1
        if debug:
            print('Attributes row after clearing those that start with error: ', str(attributes_row))
            
    #TODO: Add the code that initializes the attributes_row[] when one note is already finished 
    # Since it was found that there are some CJM docs with multiple notes
    
        
    # Add the last attributes_row to the list
    multiple_attributes_rows.append(attributes_row)
    
    # Add the sourcepath to the attributes_row
    for attributes_row in multiple_attributes_rows:
        attributes_row[source_path_index] = file
        if residential_mortgages_flag:
            attributes_row[loan_number_index] = file.split("/")[len(file.split("/"))-1].split("_")[0]
            attributes_row[-1] = file.split("/")[len(file.split("/"))-1].split("_")[1]

    # print(multiple_attributes_rows)
    
    return multiple_attributes_rows
    


# In[3]:

import os
import os.path
from os import listdir
import csv

debug = False
residential_mortgages_flag = False

reocr_files_flag = False

if reocr_files_flag:
    set_ocr = 'CJM_Notes_ReOCR'
else:
    set_ocr = 'CJM_Notes_Good_OCR'

    
cjm_indices = [source_path_index, loan_type_index, payment_type_index, mortgage_date_index,               productions_fund_date_index, usps_full_address_index, usps_city_index, usps_state_index,               usps_zip_index, loan_amount_index, note_rate_index, arm_initial_rate_index,                first_payment_date_index, interest_only_at_origination_flag_index, interest_only_exp_date_index,                maturity_date_index, initial_rate_period_index, loan_term_index,                interest_only_term_index, change_date_index, arm_payment_reset_freq_index,               arm_index_index, arm_margin_at_origination_index, arm_periodic_rate_cap_index,               arm_periodic_rate_floor_index, arm_lifetime_rate_cap_index,               arm_lifetime_rate_floor_index, arm_lifetime_rate_ceiling_index, paragraphs_not_found_index]

cjm_notes_header =   [''] * len(cjm_indices)      
cjm_index = 0
for cjm_ind in cjm_indices:
    cjm_notes_header[cjm_index] = notes_header[cjm_ind]
    cjm_index += 1
    

# if residential_mortgages_flag:
#     notes_list_file_name = '/apps/incoming/RM_Notes_Files.txt'
#     out_file_name = '/apps/incoming/RM_Notes_PSM4_Output.txt'  
#     first_path = '/apps/incoming//pendo-ocr2/psm4/notes/'
#     end_path = '.txt'
# #     out_file_name = '/apps/incoming/RM_Notes_Original_Output.txt'  
# #     first_path = '/apps/incoming//pendo-ocr/notes/'
# #     end_path = ''

#     out_file = open(out_file_name, "w", newline = '')  
#     writer = csv.writer(out_file, quoting=csv.QUOTE_ALL, escapechar='\\', quotechar='\"', delimiter = '\t')
#     writer.writerow(notes_header)

# else:
#     notes_list_file_name = '/apps/incoming/' + set_ocr + '_Files.txt'
#     out_file_name = '/apps/incoming/' + set_ocr + '_Out.txt'
#     first_path = ''
#     out_file = open(out_file_name, "w", newline = '')  
#     writer = csv.writer(out_file, quoting=csv.QUOTE_ALL, escapechar='\\', quotechar='\"', delimiter = '\t')
#     writer.writerow(cjm_notes_header)

    
# in_file = open(notes_list_file_name, 'r')
# notes = in_file.readlines()
# print(len(notes))
# in_file.close()

# if residential_mortgages_flag:
#     notes = [note for note in notes if 'Note-Note' in note or 'Note-CEMA' in note and 'HELOC' not in note]
#     print(len(notes))


# count = 0
# for note in notes[1:]:
# # First one is the column name
#     if residential_mortgages_flag:
#         note = note.split('/')[len(note.split('/'))-1]
#         note = first_path + note + end_path
    
#     if reocr_files_flag:
#         first_path = '/apps/incoming/CJM Phase 3 ReOCRd Files/'
#         note = note.split('/')[len(note.split('/'))-1]
#         note = first_path + note
#         note = note.replace('.txt.txt', '.txt')

        
#     note = note.replace('\n', '')
#     print('PROCESSING FILE: ' + note)
#     print('COUNT: ' + str(count))
#     count += 1
#     multiple_attributes_rows = extractNoteAttributes(note)
#     if residential_mortgages_flag:
#         writer.writerows(multiple_attributes_rows)
#     else:
#         cjm_multiple_attributes_rows = []
#         for attributes_row in multiple_attributes_rows:
#             cjm_attributes_row = [''] * len(cjm_indices)
#             cjm_index = 0
#             for cjm_ind in cjm_indices:
#                 cjm_attributes_row[cjm_index] = attributes_row[cjm_ind]
#                 cjm_index += 1
                
#             cjm_multiple_attributes_rows.append(cjm_attributes_row)
        
#         writer.writerows(cjm_multiple_attributes_rows)

# out_file.close()

##########
debug = True
multiple_attributes_rows = extractNoteAttributes('/apps/incoming/cjm/ocr_out/2343240835.TIF.txt')

if residential_mortgages_flag:
    print(multiple_attributes_rows)
    print(len(multiple_attributes_rows))

else:
    cjm_multiple_attributes_rows = []
    for attributes_row in multiple_attributes_rows:
        cjm_attributes_row = [''] * len(cjm_indices)
        cjm_index = 0
        for cjm_ind in cjm_indices:
            cjm_attributes_row[cjm_index] = attributes_row[cjm_ind]
            cjm_index += 1

        cjm_multiple_attributes_rows.append(cjm_attributes_row)
    
    print(cjm_multiple_attributes_rows)


# In[ ]:



