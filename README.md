# DNA-Analyzer
load, analyze, manipulate and save DNA sequences

## Description
The system will interact with the user through a CLI (Command Line Interface) that
uses the standard I/O. Using that interface, the user will be able to load DNA
sequences from files, to analyze them, to manipulate them (e.g., by extracting
sequence slices or by modifying the sequence), and to store modified sequences and
reports.
The commands are detailed in the following sections

### The Command Line Interface (CLI)
The command line interface allows interaction with the user. Throughout that
interface, the user can enter their input and see the application's output. The prompt
of the CLI is usually > cmd >>> ; it might change when special type of input is
required.\
There are several groups of commands, which are detailed in the next chapters.
Sequences
The application's most important elements are sequences . These are DNA sequences
(composed of the four characters A , C , T and G ). Each sequence that is held in the app's
memory has a name and sequence number . When referring to a sequence in
commands, unless otherwise defined, it is possible to refer it either by its ID or by its
name .\
Reference to the sequence number is done using the h ash character #\
For example:\
  #1 means sequence number 1 .\
  #107 means sequence number 107 .\
Reference to the sequence name is done using the a t character @\
For example:\
  @short-seq refers to the sequence named short-seq.\
  @dolly-dna refers to the sequence named dolly-dna .
### Files
The application stores and reads DNA sequences from files. It will use raw DNA data,
that is, files that contain the four letters and nothing else.
The default file extension for that app is .rawdna .\
Common CLI markings\
● [argument] - Words starting with " [ ", ending with " ] " represent optional
arguments.\
● <argument> - Words starting with " < ", ending with " > " represent required
arguments.\
● arg1|arg2 - Pipe sign ("|") between words represents that each one of them can
be used.\
Example using bash command cp :\
 ```
cp [-r|-f] <source> [<source2> [<source3> ...]] <destination>
 ```
Means that:\
● cp can be used with flag -r or with flag -f, but they both are optional.\
● After the flags (if they exist) must be the source files. At least one, but
can be many.\
● At the end must be the destination\
Legal examples:
```
cp x.cpp dna.cpp
cp -r project dnaProject
cp -f y.cpp dna.cpp
cp dna.cpp dna.h dnaProject
```

##  Sequence Creation Commands
The following commands are being used to generate new sequences :
### new
 ```
> cmd >>> new <sequence> [@<sequence_name>]
  ```
Creates a new sequence, as described by the followed sequence.
If the @<sequence_name> is used, then this will be the name of the new sequence.
Otherwise, a default name will be provided - seq1 (or seq2 , seq3 and so on, if the
name is already taken).
The new sequence, its name and its number (internal ID, starting with 1) are
printed.
For example:
   ```
> cmd >>> new ATACTGCCTGAATAC @short_seq
  ```
will create that sequence;
if this is the first sequence, it will be numbered "1" and the following will be
printed:
  ```
[ 1 ] short_seq: ATACTGCCTGAATAC
  ```
### load
   ```
> cmd >>> load <file_name> [@<sequence_name>]
  ```
loads the sequence from the file, assigns it with a number (ID) and a default name, if
one was not provided (based on the file name, possibly postfixed with a number if the
name already exists), and prints it.
For example:
  ```
> cmd >>> load my_dna_seq.rawdna
  ```
will load the sequence from the file my_dna_seq.rawdna and will print its
assigned ID, its name and the sequence (no more than 40 chars; If there are
more in the sequence, it prints the first 32, then an ellipsis, and then the last
three ones). So, a typical output might be:
  ```
[ 14 ] my_dna_seq: AACGTTTTTGAACACCAGTCAACAACTAGCCA...TTG
  ```
### dup
   ```
> cmd >>> dup <seq> [@<new_seq_name>]
  ```
duplicates the sequence.
If a new name is not provided, then it will be based on the name of <seq> , suffixed
by _1 (or _2 , _3 , ... if the name is already taken).
For example:
  ```
> cmd >>> dup # 22
  ```
will result in
  ```
[ 23 ] conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT
  ```
  
 ## Sequence Manipulation Commands
The following commands manipulate existing sequences :
Their default behavior is to modify the source sequence in-place (that is, the
original ID and name of the sequence are left the same, only its content is
modified).\
● If a colon : appears after the command's argument, then the original
sequence is left untouched, and a new sequence is generated with the
manipulation results.\
● If an argument of the form @<new_seq_name> is provided after the colon, then
this is the name of the new sequence.
● Otherwise, if @@ instead, then the name of the new sequence is automatically
generated by the app.\
Each command might generate a different default name.
When a sequence is required as a source, both ID ( #<seq_id> ) or name ( @seq_name )
are acceptable, unless otherwise defined.
### slice
   ```
> cmd >>> slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
  ```
Slices the sequence, so that starts in <from_ind> (0-based index) and ends in <to_ind
(inclusive ).\
If @<new_seq_name is provided, the results will create a new sequence with that name.\
If @@ is provided, the results will create a new sequence with auto-generate name,
based on the name of the original sequence, with the suffix _s1 (or, if that name is
already occupied, with the suffix _s2 , and so on).\
For example:\
Assuming that the former short_seq 's ID is 1, the following command:
   ```
> cmd >>> slice # 1 4 9
  ```
will change the sequence to TGCCT (Letters at indices 4,5,6,7,8) and print the
output:
  ```
[ 1 ] short_seq: TGCCT
  ```
If @@ was provided to the same command, then sequence 1 would have not changed,
and a new sequence would have been generated instead.
A typical call, then, might look like:
  ```
> cmd >>> slice # 1 4 8 : @@
[ 19 ] short_seq_s1: TGCCT
  ```
### replace
  ```
> cmd >>> replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]
  ```
replaces the letter in the (0-based) index of <seq> by <new_letter> .\
If @<new_seq_name> is provided, the original sequence is left untouched and the
result is put in a newly created sequence with that name.\
If @@ is provided, the name is based on the original sequence, with the suffix _r1 (or,
if that name is already existing, _r2 and so on).\
The command might get more than a single replacement. In that case, after <seq>
there will be more than one pair of <index> and <new_letter> .
For example:
   ```
> cmd >>> replace @short_seq_s1 0 A 3 A : @repl_seq
  ```
will result in the following output:
  ```
[ 20 ] repl_seq: AGCAT
  ```

### del
  ```
> cmd >>> del <seq>
  ```
deletes that sequence.
Before deleting it, the user is asked to confirm that:
Confirmation is done by entering y or Y , Entering n or N cancels the deletion. Any
other input will result in a message that asks the user again to confirm the deletion.
Once confirmed, the sequence is deleted and a message is printed. Otherwise, a
cancellation message is printed.
So, a deletion scenario might look like:
  ```
> cmd >>> del # 23
Do you really want to delete conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT?
Please confirm by 'y' or 'Y' , or cancel by 'n' or 'N' .
> confirm >>> x
You have typed an invalid response. Please either confirm by 'y' / 'Y' , or
cancel by 'n' / 'N' .
> confirm >>> Y
Deleted: [ 23 ] conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT
  ```



## Batch Commands
### Batch Creation
  ```
> cmd >>>batch <batch_name>
  ```
Batch mode allows the user to define a series of actions that will take place one after
another.\
In order to define a batch, the user enters the command batch , followed by the name
of that new batch. Then, it enters into batch mode , where any command is not being
activated immediately, but rather, entered into the batch.\
The command end ends the batch mode.\
For example:

> cmd >>> batch my_batch
> batch >>> load basil_dna.rawdna @basil
> batch >>> pair basil @basil_pair
> batch >>> slice @basil_pair 0 4 @basil_interesting_part
> batch >>> save @basil_pair
> batch >>> end
> cmd >>>
This batch (when run) will load a sequence from the file basil_dna.rawdna and will keep it under the name basil.

Then, it will create its pair and keep it under the name basil_pair.

After that, it will slice it to the first forth nucleodites. That slice will be kept under the name basil_interesting_part and then will be saved to disk using that name (with the .rawdna suffix).

When the batch mode ends, the batch is added to the list of active batches - nothing is being activated yet.

### Running Batches
The command run <@batchname> runs a batch, that is, executes it as if the
commands were entered manually.
### Listing Batches
The command batchlist shows a list of all the batch names.
### Showing a Batch
The command batchshow <@batch_name> shows the content of that batch.
### Saving Batches
Saving a batch is done using the command batchsave , followed by the filename.
If the filename is omitted, then the batch name is being used as the filename, with the
suffix .dnabatch
The batch is saved exactly as it is written in the CLI (without the prompt, of course).
Thus, for example:
The above script will be saved as:
  ```
load basil_dna.rawdna @basil
pair basil @basil_pair
find ## TGATTCTC : @start_slice
find ## TTTTAAAATTTTCCCC
calc __ + 4
slice @basil_pair @start_slice __ @basil_interesting_part
save ##
  ```
### Loading Batches
Loading a batch is done using the command batchload , followed by the filename to
be loaded.
The loaded batch will have that name (without the .dnabatch suffix, if appears). If
the command is followed by : @<batch_name> , then it will be kept as batch_name .
